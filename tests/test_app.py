from fastapi.testclient import TestClient
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

# Mock redis before importing app
from unittest.mock import MagicMock, patch
import main

def test_health_with_redis_mock():
    with patch.object(main.r, 'ping', return_value=True):
        from fastapi.testclient import TestClient
        client = TestClient(main.app)
        response = client.get("/health")
        assert response.status_code == 200

def test_root():
    from fastapi.testclient import TestClient
    client = TestClient(main.app)
    response = client.get("/")
    assert response.status_code == 200
    assert "URL Shortener" in response.json()["message"]
