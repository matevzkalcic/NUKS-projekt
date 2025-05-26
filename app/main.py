from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app import database, models

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.on_event("startup")
def startup():
    database.create_tables()

@app.get("/")
def read_root(request: Request):
    tasks = database.get_tasks()
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.post("/add")
def add_task(title: str = Form(...)):
    database.add_task(title)
    return RedirectResponse(url="/", status_code=303)

@app.post("/complete/{task_id}")
def complete_task(task_id: int):
    database.complete_task(task_id)
    return RedirectResponse(url="/", status_code=303)

@app.get("/stats")
def get_stats():
    return database.get_stats()

@app.post("/delete/{task_id}")
def delete_task(task_id: int):
    database.delete_task(task_id)
    return RedirectResponse(url="/", status_code=303)