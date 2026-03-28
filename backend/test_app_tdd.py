import pytest
from fastapi.testclient import TestClient
from app import app
import time

client = TestClient(app)

def test_headlines_endpoint_structure():
    response = client.get("/api/headlines")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    for source in ["timesofisrael", "ynet", "jpost"]:
        assert source in data
        assert isinstance(data[source], dict)
        assert "headlines" in data[source]
        assert isinstance(data[source]["headlines"], list)
        assert len(data[source]["headlines"]) <= 10
        for h in data[source]["headlines"]:
            assert "title" in h
            assert isinstance(h["title"], str)
            assert "published" in h
            assert isinstance(h["published"], str)
        assert "last_fetch" in data[source]
        # last_fetch should be ISO8601 string, parseable by time.strptime
        try:
            time.strptime(data[source]["last_fetch"], "%Y-%m-%dT%H:%M:%SZ")
        except Exception:
            assert False, f"last_fetch not ISO8601: {data[source]['last_fetch']}"
