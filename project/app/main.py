from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional, List

from app.config import get_settings, Settings


class Todo(BaseModel):
    id: int
    title: str


app = FastAPI(title="TDD Todo API")

store_todo = []


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing,
    }


@app.post("/todo/", status_code=201)
async def create_todo(todo: Todo):
    store_todo.append(todo)
    return todo

@app.get("/todo/", response_model=List[Todo])
async def get_all_todos():
    return store_todo

