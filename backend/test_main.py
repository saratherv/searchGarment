from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_item_base_case():
    response = client.get("/search?searchValue=H%26M&offset=0")
    assert response.status_code == 200
    assert response.json()["code"] == 200
    assert len(response.json()["data"]) == 50

def test_read_item_error_case():
    response = client.get("/search?searchValue=sk&offset=0")
    assert response.status_code == 200
    assert response.json()["code"] == 500

def test_read_item_without_offset():
    response = client.get("/search?searchValue=H%26M")
    assert response.status_code == 200
    assert response.json()["success"] == True
    assert len(response.json()["data"]) == 50

    