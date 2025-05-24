import streamlit as st
import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from rapidfuzz import process, fuzz



# Load companies and keywords from CSV
def load_company_data(filepath='Company.csv'):
    df = pd.read_csv(filepath)
    company_map = {}

    for _, row in df.iterrows():
        ticker = row['Ticker'].strip().upper()
        english = row['EnglishName'].strip()
        hindi_raw = str(row['HindiName'])
        hindi_names = [name.strip() for name in hindi_raw.split(',') if name.strip()]
        all_names = [english] + hindi_names

        # Map ticker and English name to all names
        company_map[ticker] = all_names
        company_map[english.upper()] = all_names

    return company_map


    
# Expand user input based on CSV
def expand_stock_list(stock_list, company_map):
    expanded = []
    for keyword in stock_list:
        key = keyword.strip().upper()
        if key in company_map:
            # Expand to all mapped names (English + Hindi variants)
            expanded.extend(company_map[key])
        else:
            # Use the keyword itself directly if not in CSV
            expanded.append(keyword.strip())
    # Remove duplicates
    return list(set(expanded))


# Fetch transcript using YouTubeTranscriptApi
def get_transcript(video_id):
    try:
        return YouTubeTranscriptApi.get_transcript(video_id, languages=['hi', 'en'])
    except (TranscriptsDisabled, NoTranscriptFound):
        st.error("Transcript disabled or not found.")
    except Exception as e:
        st.error(f"Error fetching transcript: {e}")
    return None

# Fuzzy search for keywords in transcript
def search_stock_in_transcript(transcript, stock_list):
    timestamps = []
    for entry in transcript:
        text = entry['text'].lower()
        for stock in stock_list:
            match, score, _ = process.extractOne(
                stock.lower(),
                [text],
                scorer=fuzz.partial_ratio
            )
            if score >= 80:
                timestamps.append((entry['start'], stock, text))
    return timestamps

# Generate time-stamped YouTube link
def create_youtube_link(video_id, timestamp):
    return f"https://www.youtube.com/watch?v={video_id}&t={int(timestamp)}s"

# Streamlit App UI
def main():
    st.title("📊 FuzzyTube")
    video_url = st.text_input("🔗 Enter YouTube Video URL")
    stock_input = st.text_input("🔍 Enter stock names, tickers, or keywords (comma-separated)")

    if st.button("Search"):
        if not video_url or not stock_input:
            st.warning("Please enter both a YouTube URL and stock keywords.")
            return

        video_id = video_url.split("v=")[-1].split("&")[0]  # robust extraction
        transcript = get_transcript(video_id)
        if transcript:
            company_map = load_company_data("Company.csv")  # your CSV filename
            stock_list = [stock.strip() for stock in stock_input.split(",")]
            expanded_stocks = expand_stock_list(stock_list, company_map)
            timestamps = search_stock_in_transcript(transcript, expanded_stocks)
            if timestamps:
                for ts, keyword, line in timestamps:
                    link = create_youtube_link(video_id, ts)
                    st.write(f"[{keyword}]({link})-{line}")
            else:
                st.write("No stock mentions found.")
        else:
            st.write("Transcript not available.")

if __name__ == "__main__":
    main()
