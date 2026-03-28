# Plan: News Aggregation and Summarization with LLM, Source Attribution, and Summary Header

**Target Release:** v0.7.0
**Epic Alignment:** News Aggregation, LLM Integration, Source Attribution
**Status:** Active
**Changelog:**
- 2026-03-29: Initial plan created for LLM-powered news aggregation, source attribution, and summary header (Planner agent).

---

## Value Statement and Business Objective

As a news consumer, I want to see a concise, AI-generated summary of the latest news, with each news item attributed to its original source, so that I can quickly understand the main stories and their origins in a single, trustworthy view.

---

## Objective

- Aggregate news from multiple sources.
- Use Groq API (llama-3.1-8b-instant) via LangGraph to summarize and attribute news.
- Generate a short summary header for the aggregated news.
- Expose this data via the backend API.
- Display the summary header and attributed sources in the frontend.

---

## Assumptions

- Groq API key and endpoint are available and will be stored securely (e.g., in `.env`).
- News sources are accessible via public APIs or RSS feeds.
- LangGraph is compatible with the backend stack (Python).
- Frontend can be updated to display new data structures.
- No user authentication is required for this feature.
- News aggregation is performed on-demand (not scheduled/background).

---

## Plan

### 1. Backend: News Aggregation and Summarization

**1.1. Add/Update Dependencies**
- Add `langgraph` for orchestration.
- Add `requests` or `httpx` for fetching news sources.
- Add Groq API client (if not included in LangGraph).
- Ensure `python-dotenv` is present for local development.
- Update `requirements.txt` accordingly.

**1.2. Configuration**
- Add `.env` variables for Groq API key and endpoint.
- Add configuration for news source URLs.

**1.3. News Fetching Module**
- Implement a module to fetch news from multiple sources (APIs/RSS).
- Normalize news items (title, content, source, timestamp).

**1.4. LangGraph Orchestration**
- Create a LangGraph workflow:
  - Input: List of news items (title, content, source).
  - Step 1: Aggregate and summarize news using Groq LLM.
  - Step 2: Attribute each summarized item to its source.
  - Step 3: Generate a short summary header for the entire batch.
- Ensure LLM prompt includes instructions for source attribution and summary header.

**1.5. API Endpoint**
- Add a new endpoint (e.g., `/api/aggregated-news`) that:
  - Fetches news from sources.
  - Runs the LangGraph workflow.
  - Returns: `{ summary_header, items: [{ summary, source, url }] }`.

**1.6. Error Handling & Logging**
- Handle API failures, LLM errors, and timeouts gracefully.
- Log errors for debugging.

---

### 2. Frontend: Display Aggregated News

**2.1. API Integration**
- Fetch data from `/api/aggregated-news`.

**2.2. UI Updates**
- Display the summary header prominently.
- List each summarized news item with its attributed source (and link if available).
- Ensure responsive and accessible design.

**2.3. Loading/Error States**
- Show loading indicator while fetching.
- Display user-friendly error messages on failure.

---

### 3. Documentation

- Update `README.md` with setup instructions for new dependencies, environment variables, and API usage.

---

### 4. Version Management

- Update version to v0.7.0 in all relevant files (`package.json`, `requirements.txt`, etc.).
- Add a CHANGELOG entry describing the new feature.

---

## Testing Strategy

- **Backend:** Unit tests for news fetching, LangGraph workflow, and API endpoint. Mock LLM and news sources for deterministic tests.
- **Frontend:** Integration test for API consumption and UI rendering. Manual verification for summary/header display and source attribution.
- **Critical Scenarios:** LLM failure, missing sources, malformed news data, slow responses.

---

## Validation

- API returns aggregated news with summary header and attributed sources.
- Frontend displays summary header and attributed news items with sources.
- All new dependencies and configuration are documented and functional.

---

## Risks

- LLM may hallucinate or misattribute sources—prompt engineering and validation required.
- News source APIs may change or become unavailable.
- LLM API costs and rate limits.
- Latency if aggregation is slow—may require caching or async processing in future.

---

## OPEN QUESTIONS

- **None blocking.** All requirements are clear for initial implementation.

---

## Handoff

- After Critic review, proceed to implementation.
- Ensure all new dependencies are installed and documented.
- Coordinate with QA for test coverage and validation.

---

**Ready for Critic review.**
