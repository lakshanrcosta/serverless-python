# File: app/api/todos.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.todo import TodoController
from app.schemas.todo import TodoCreate, TodoUpdate, TodoResponse
from app.database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=TodoResponse)
def create_todo(todo_create: TodoCreate, db: Session = Depends(get_db)):
    return TodoController.create(todo_create, db)

@router.get("/", response_model=List[TodoResponse])
def get_all_todos(db: Session = Depends(get_db)):
    return TodoController.get_all(db)

@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    return TodoController.get(todo_id, db)

@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo_update: TodoUpdate, db: Session = Depends(get_db)):
    return TodoController.update(todo_id, todo_update, db)

@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    return TodoController.delete(todo_id, db)
