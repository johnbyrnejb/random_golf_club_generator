from fastapi import FastAPI

from app.random_club_generator import select_random_club

app = FastAPI()


@app.get("/select_club")
async def root():
    return select_random_club()