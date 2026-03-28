import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_aggregated_news_endpoint_structure():
    response = client.get("/api/aggregated-news")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "summary_header" in data
    assert isinstance(data["summary_header"], str)
    assert "items" in data
    assert isinstance(data["items"], list)
    for item in data["items"]:
        assert "summary" in item
        assert isinstance(item["summary"], str)
        assert "source" in item
        assert isinstance(item["source"], str)
        assert "url" in item
        assert isinstance(item["url"], str)
