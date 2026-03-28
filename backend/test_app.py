import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_headlines_endpoint():
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
