from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from ..entities import Tasks
from ..schemas import CreateTask, ResponseTask, UpdateTask


def create_new_task(task: CreateTask, db: Session) -> ResponseTask | None:
    new_task = Tasks(**task.model_dump())
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task


def retrieve_task(task_id: int, db: Session) -> ResponseTask | None:
    return db.query(Tasks).filter(Tasks.id == task_id).first()


def retrieve_all_task(db: Session) -> list:
    return db.query(Tasks).all()


def update_task(task_id: int, update: UpdateTask, db: Session) -> ResponseTask | None:
    task = db.query(Tasks).filter(Tasks.id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task does not exist")
    
    for k, v in update.model_dump(exclude_unset=True).items():
        setattr(task, k, v)

    db.commit()
    db.refresh(task)
    return task


def delete_task(task_id: int, db: Session) -> ResponseTask | None:
    task = db.query(Tasks).filter(Tasks.id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task does not exist")
    db.delete(task)
    db.commit()
    
    return task
