# File: app/services/todos.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.todo import TodoRepository
from app.schemas.todo import TodoCreate, TodoUpdate

class TodoService:

    @staticmethod
    def create_todo(db: Session, todo_create: TodoCreate):
        return TodoRepository.create(db, todo_create)

    @staticmethod
    def get_all_todos(db: Session):
        return TodoRepository.get_all(db)

    @staticmethod
    def get_todo_by_id(db: Session, todo_id: int):
        todo = TodoRepository.get_by_id(db, todo_id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo

    @staticmethod
    def update_todo(db: Session, todo_id: int, todo_update: TodoUpdate):
        todo = TodoRepository.get_by_id(db, todo_id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        return TodoRepository.update(db, todo, todo_update)

    @staticmethod
    def delete_todo(db: Session, todo_id: int):
        todo = TodoRepository.get_by_id(db, todo_id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        TodoRepository.delete(db, todo)
