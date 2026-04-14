from fastapi.testclient import TestClient
from unittest.mock import patch
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

def test_health_with_redis_mock():
    with patch("main.r.ping", return_value=True):
        import main
        client = TestClient(main.app)
        response = client.get("/health")
        assert response.status_code == 200

def test_health_redis_down():
    with patch("main.r.ping", side_effect=Exception("Redis down")):
        import main
        client = TestClient(main.app)
        response = client.get("/health")
        assert response.status_code == 500

def test_root():
    import main
    client = TestClient(main.app)
    response = client.get("/")
    assert response.status_code == 200
    assert "URL Shortener" in response.json()["message"]
