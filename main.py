from fastapi import FastAPI
from models import Todo

app = FastAPI()

todos = [
    Todo(id=1, name= 'first task', description= 'this is a first task'),
    Todo(id=2, name= 'second task', description= 'this is a second task')
]

@app.get("/")
def handshake():
    return 'app is working fine'

@app.get("/todo")
def get_todolist():
    return todos;

@app.post("/todo")
def add_item(item:Todo):
    todos.append(item)
    return "item added successfully"

@app.put("/todo/{id}")
def update_item(id: int, item: Todo):
    for index, todo in enumerate(todos):
        if todo.id == id:
            todos[index] = item
            return "item updated successfully"

    return "item not found"

@app.get("/todo/{id}")
def getItem(id:int):
    for todo in todos:
        if todo.id == id:
            return todo

    return "item not found"

@app.delete("/todo/{id}")
def removeItem(id:int):
    for index, item in enumerate(todos):
        if item.id == id:
            del todos[index]
            return 'item deleted successfully'

    return "item not found"
        