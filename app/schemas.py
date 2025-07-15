from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Task(BaseModel):
    title: str
    description: str


class CreateTask(Task):
    pass


class ResponseTask(Task):
    id: int
    completed: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
    
    
class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    
    class Config:
        from_attributes = True
