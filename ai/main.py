import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from src.db.db import lifespan
from src.api import api_router

app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


@app.get("/")
async def root():
    return {"Hello": "AI Dungeon Master API"}


if __name__ == "__main__":
    load_dotenv()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
