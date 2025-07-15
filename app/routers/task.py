from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..dependencies import tasks
from ..entities import Tasks
from ..schemas import CreateTask, ResponseTask, UpdateTask

task_route = APIRouter()


@task_route.post("/", response_model=ResponseTask, status_code=status.HTTP_201_CREATED)
def create(task: CreateTask, db: Session = Depends(get_db)) -> ResponseTask:
    try:
        new_task = tasks.create_new_task(task, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return new_task


@task_route.get("/", response_model=List[ResponseTask], status_code=status.HTTP_200_OK)
def retrieve_all(db: Session = Depends(get_db)):
    return tasks.retrieve_all_task(db)


@task_route.get("/{task_id}", response_model=ResponseTask, status_code=status.HTTP_200_OK)
def retrieve(task_id: int, db: Session = Depends(get_db)):
    task = tasks.retrieve_task(task_id, db)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@task_route.patch("/{task_id}", response_model=ResponseTask, status_code=status.HTTP_200_OK)
def edit_task(task_id: int, update: UpdateTask, db: Session = Depends(get_db)):
    if task_id:
        return tasks.update_task(task_id, update, db)


@task_route.delete("/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int, db: Session = Depends(get_db)) -> dict:
    task = tasks.delete_task(task_id, db)
    if task:
        return {"message": f"Task '{task.title}' deleted successfully"}
