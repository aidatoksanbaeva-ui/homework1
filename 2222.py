from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import uvicorn

app = FastAPI()

todos = {}

class Todo(BaseModel):
    text: str
    done: bool = False
    category: str = "Басқа"


@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def add_todo(todo: Todo):
    todo_id = str(uuid.uuid4())
    todos[todo_id] = todo
    return {"id": todo_id, **todo.dict()}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: str, new_todo: Todo):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Тапсырма жоқ")

    todos[todo_id] = new_todo
    return {"id": todo_id, **new_todo.dict()}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Тапсырма жоқ")

    del todos[todo_id]
    return {"message": "Өшірілді"}
if __name__ == "__main__":
    uvicorn.run(app, port=9959)