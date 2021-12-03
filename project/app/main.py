from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings, Settings


class Todo(BaseModel):
    id: int
    title: str


app = FastAPI(title="TDD Todo API")
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

