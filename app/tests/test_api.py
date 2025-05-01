# tests/test_api.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_todo():
    response = client.post("/todos/", json={"title": "Buy milk"})
    assert response.status_code == 200
    assert response.json()["title"] == "Buy milk"
    global todo_id
    todo_id = response.json()["id"]

def test_get_all_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_todo_by_id():
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["id"] == todo_id

def test_update_todo():
    response = client.put(f"/todos/{todo_id}", json={"title": "Buy eggs"})
    assert response.status_code == 200
    assert response.json()["title"] == "Buy eggs"

def test_delete_todo():
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 200
