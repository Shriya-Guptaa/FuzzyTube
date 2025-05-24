# FuzzyTube

## Overview

This Streamlit web app lets you input a YouTube video URL and search for **stock mentions** or any keywords (in English or Hindi) within the video's transcript. It supports fuzzy keyword matching and displays timestamped YouTube links to each stock mention.

---

## Features

- Accepts stock names or tickers in **English or Hindi**
- Matches stock mentions using **fuzzy text search**
- Supports YouTube videos with **English or Hindi transcripts**
- Outputs **timestamped links** to where the stock is mentioned
- Automatically expands keywords using a company mapping CSV

---

![image alt](https://github.com/Shriya-Guptaa/FuzzyTube/blob/main/Screenshot1(hindi).png?raw=true)
![image alt](https://github.com/Shriya-Guptaa/FuzzyTube/blob/main/Screenshot2(english).png?raw=true)


## Requirements

- Python 3.7+
- Streamlit
- pandas
- youtube-transcript-api [@jdepoix]
- rapidfuzz


---
## Installation  

### Prerequisites  
- Python 3.7 or higher  
- Pip (Python package manager)  

### Steps  
1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/Shriya-Guptaa/FuzzyTube
   cd FuzzyTube
   
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run the Application:**
   ```bash
    streamlit run app.py

4. **Access the Web App:**
    Open your browser and visit http://localhost:8501 to start using FuzzyTube
---
## Usages
- **Input YouTube Video URL:** Paste the link to a video with English or Hindi subtitles.

- **Enter Stock Keywords:** Add stock names, tickers, or company keywords (comma-separated).

- **Search Transcripts:** Click the Search button to find mentions using fuzzy matching.

- **Explore Results:** View timestamped clickable links directing to exact moments stocks are mentioned.

- **Customize Keywords:** Update the Company.csv file to add or edit company names and aliases in English and Hindi.

## 📚 Dependencies & Acknowledgements

This app uses the excellent [`youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api) library by [@jdepoix](https://github.com/jdepoix) for fetching YouTube transcripts.

## License
This project is licensed under the MIT License.


