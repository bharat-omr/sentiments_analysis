# sentiments_analysis_with_python_fast_api_or_llm

## REST API

![Screenshot 2025-05-27 113407](https://github.com/user-attachments/assets/f1c12257-b98e-4099-b965-0fd0492f6a95)

## MONGODB DATA SAVE 

![Screenshot 2025-05-27 113349](https://github.com/user-attachments/assets/c0e135f2-80ef-4ff2-ad1e-d113a9e1f83a)

## prompt 

![image](https://github.com/user-attachments/assets/6298e76d-4e72-490c-88df-f953fa86c544)



# Product Review Analyzer

This project analyzes product reviews using an LLM (Gemini) and provides:

- **Sentiment Analysis** (Positive, Negative, Neutral)
- **Key Phrase Extraction**
- **Suggestions for Improvement**

## 🧠 Backend (FastAPI + MongoDB + Gemini)

### Features
- REST API: `/analyze-review` for review analysis
- Gemini LLM integration
- Async MongoDB storage with Motor
- JWT authentication (optional) Currently not add this.
- Endpoint: `/history` to fetch previous analyses

### Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/bharat-omr/sentiments_analysis.git
   cd review-analyzer/backend


## Create a .env file:


GOOGLE_API_KEY ="YOUR KEY"


MONGODB_URL=mongodb+srv://<user>:<password>@cluster0.mongodb.net/
