from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import feedparser
from dotenv import load_dotenv
import os
import pathlib
from datetime import datetime, timezone

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

frontend_path = str(pathlib.Path(__file__).parent.parent / "frontend")
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/")
def serve_index():
    return FileResponse(pathlib.Path(frontend_path) / "index.html")

FEEDS = {
    "timesofisrael": "https://www.timesofisrael.com/feed/",
    "ynet": "https://www.ynet.co.il/Integration/StoryRss2.xml",
    "jpost": "https://www.jpost.com/Rss/RssFeedsHeadlines.aspx"
}

@app.get("/api/headlines")
def get_headlines():
    result = {}
    for name, url in FEEDS.items():
        d = feedparser.parse(url)
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        items = []
        for entry in d.entries[:10]:
            published = None
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                published = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            elif hasattr(entry, "published"):
                published = entry.published
            else:
                published = now
            items.append({
                "title": entry.title,
                "published": published
            })
        result[name] = {
            "headlines": items,
            "last_fetch": now
        }
    return JSONResponse(result)
