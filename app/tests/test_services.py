# tests/test_services.py

from app.schemas.todo import TodoCreate, TodoUpdate
from app.services.todo import TodoService
from unittest.mock import MagicMock

def test_create_todo_service():
    db = MagicMock()
    todo_data = TodoCreate(title="Read book")
    result = TodoService.create_todo(db, todo_data)
    db.add.assert_called_once()
    db.commit.assert_called_once()
    assert result.title == "Read book"

def test_update_todo_service():
    db = MagicMock()
    db_todo = MagicMock()
    db.query().filter().first.return_value = db_todo
    update_data = TodoUpdate(title="Updated")
    result = TodoService.update_todo(db, 1, update_data)
    assert db_todo.title == "Updated"
    db.commit.assert_called_once()

def test_delete_todo_service():
    db = MagicMock()
    db.query().filter().first.return_value = MagicMock()
    result = TodoService.delete_todo(db, 1)
    db.delete.assert_called_once()
    db.commit.assert_called_once()

def test_get_todo_service():
    db = MagicMock()
    mock_todo = MagicMock()
    db.query().filter().first.return_value = mock_todo
    result = TodoService.get_todo_by_id(db, 1)
    assert result == mock_todo

def test_get_all_todos_service():
    db = MagicMock()
    db.query().all.return_value = ["todo1", "todo2"]
    result = TodoService.get_all_todos(db)
    assert result == ["todo1", "todo2"]
