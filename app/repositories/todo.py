# File: app/repositories/todos.py

from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate

class TodoRepository:

    @staticmethod
    def create(db: Session, todo_create: TodoCreate) -> Todo:
        db_todo = Todo(**todo_create.model_dump())
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo

    @staticmethod
    def get_all(db: Session) -> list[Todo]:
        return db.query(Todo).all()

    @staticmethod
    def get_by_id(db: Session, todo_id: int) -> Todo | None:
        return db.query(Todo).filter(Todo.id == todo_id).first()

    @staticmethod
    def update(db: Session, db_todo: Todo, todo_update: TodoUpdate) -> Todo:
        for field, value in todo_update.model_dump(exclude_unset=True).items():
            setattr(db_todo, field, value)
        db.commit()
        db.refresh(db_todo)
        return db_todo

    @staticmethod
    def delete(db: Session, db_todo: Todo) -> None:
        db.delete(db_todo)
        db.commit()
