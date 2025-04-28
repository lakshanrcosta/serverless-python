# File: app/controllers/todos.py

from fastapi import Depends
from sqlalchemy.orm import Session
from app.services.todo import TodoService
from app.schemas.todo import TodoCreate, TodoUpdate
from app.database import get_db

class TodoController:

    @staticmethod
    def create(todo_create: TodoCreate, db: Session):
        return TodoService.create_todo(db, todo_create)

    @staticmethod
    def get_all(db: Session = Depends(get_db)):
        return TodoService.get_all_todos(db)

    @staticmethod
    def get(todo_id: int, db: Session = Depends(get_db)):
        return TodoService.get_todo_by_id(db, todo_id)

    @staticmethod
    def update(todo_id: int, todo_update: TodoUpdate, db: Session = Depends(get_db)):
        return TodoService.update_todo(db, todo_id, todo_update)

    @staticmethod
    def delete(todo_id: int, db: Session = Depends(get_db)):
        return TodoService.delete_todo(db, todo_id)