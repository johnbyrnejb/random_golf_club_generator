from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from app.random_club_generator import select_random_club
from app.retrieve_random_space import return_nasa_info

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/club", response_class=HTMLResponse)
async def return_random_club(request: Request):
    return templates.TemplateResponse("random_club.html", {"request": request, "club": select_random_club()})


@app.get("/space", response_class=HTMLResponse)
async def return_random_space(request: Request):
    return templates.TemplateResponse("random_nasa.html", {"request": request, "space": return_nasa_info()})
