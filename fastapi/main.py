from typing import TypedDict, Union

import pydantic

from fastapi import FastAPI, HTTPException

app = FastAPI()


class Todo(TypedDict):
    id: int
    title: str
    completed: bool


todo_items: list[Todo] = []


@app.get("/todos")
def list_todos():
    return todo_items


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    todo = list(filter(lambda x: x["id"] == todo_id, todo_items))
    if len(todo) < 1:
        raise HTTPException(404, "todo not found")

    return todo[0]


class CreateTodo(pydantic.BaseModel):
    title: str


@app.post("/todos")
def create_todo(todo: CreateTodo, status_code=201):
    todo_items.append(Todo(id=len(todo_items) + 1, title=todo.title))

    return todo_items[-1]


class UpdateTodo(pydantic.BaseModel):
    title: Union[str, None] = None
    completed: Union[bool, None] = None


@app.patch("/todos/{todo_id}", status_code=202)
def update_todo(todo_id: int, todo: UpdateTodo):
    todo = list(
        filter(
            lambda x: x["id"] == todo_id,
            map(
                lambda x: (
                    {**x, **todo.model_dump(exclude_none=True)}
                    if x["id"] == todo_id
                    else x
                ),
                todo_items,
            ),
        )
    )
    if len(todo) < 1:
        raise HTTPException(404, "todo not found")

    return todo[0]


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    global todo_items

    todo_items = list(filter(lambda x: x["id"] != todo_id, todo_items))
