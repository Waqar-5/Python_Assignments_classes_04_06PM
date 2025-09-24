from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.models import HabitManager
from app.database import Database

app = FastAPI()

# Templates & static files
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Database
db = Database("app/data.json")
habit_manager = HabitManager(db)

# Home/Dashboard
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    habits = habit_manager.get_all_habits()
    return templates.TemplateResponse("index.html", {"request": request, "habits": habits})

# Add Habit
@app.post("/add")
async def add_habit(name: str = Form(...), goal: int = Form(...)):
    habit_manager.add_habit(name, goal)
    return RedirectResponse("/", status_code=303)

# Delete Habit
@app.get("/delete/{habit_id}")
async def delete_habit(habit_id: int):
    habit_manager.delete_habit(habit_id)
    return RedirectResponse("/", status_code=303)

# Mark Habit as Done
@app.get("/done/{habit_id}")
async def mark_done(habit_id: int):
    habit_manager.mark_done(habit_id)
    return RedirectResponse("/", status_code=303)
