from fastapi import FastAPI

from .database import Base, engine
from .entities.tasks import Tasks
from .routers.task import task_route

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(task_route, prefix="/tasks", tags=["Task"])


@app.get("/")
def read_root():
    return {"Hello": "World"}
