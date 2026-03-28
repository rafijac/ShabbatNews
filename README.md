
# Local Israeli News Dashboard (v0.7.0)

A local dashboard for Israeli news headlines, now with LLM-powered aggregation, source attribution, and summary header. Runs with FastAPI backend and static frontend.

## Features
- Aggregates latest headlines from Times of Israel, Ynet, and JPost
- **LLM-powered summary and source attribution** using Groq API and LangGraph
- FastAPI backend exposes `/api/aggregated-news` (LLM summary) and `/api/headlines` (raw)
- Frontend displays summary header and attributed sources
- Auto-refreshes every 60 seconds

## Setup

### 1. Backend
1. Install Python 3.8+
2. Install dependencies:
   ```
   pip install -r backend/requirements.txt
   ```
3. Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   GROQ_API_ENDPOINT=https://api.groq.com/v1
   NEWS_SOURCES=https://www.timesofisrael.com/feed/,https://www.ynet.co.il/Integration/StoryRss2.xml,https://www.jpost.com/Rss/RssFeedsHeadlines.aspx
   ```
   If you do not provide a Groq API key, the backend will use a stubbed summary for local/testing.
4. Run the server:
   ```
   uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000
   ```

### 2. Frontend
No build needed. Static files are served by FastAPI at http://localhost:8000/

## Usage
- Open [http://localhost:8000/](http://localhost:8000/) in your browser.
- The dashboard displays an LLM-generated summary header and attributed news items.
- Data auto-refreshes every 60 seconds.

## API

- `/api/aggregated-news`: Returns `{ summary_header, items: [{ summary, source, url }] }` (LLM-powered)
- `/api/headlines`: Returns raw headlines by source

## Notes
- All code and data remain local unless you provide a Groq API key for LLM summarization.
- If you need to change RSS sources, edit `backend/app.py` or the `NEWS_SOURCES` in `.env`.

## Requirements
- Python 3.8+
- pip
- Groq API key (for live LLM summaries; optional for local dev)

## License
MIT
