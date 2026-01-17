import uvicorn
from fastapi import FastAPI


from dotenv import load_dotenv
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from src.llm.dungeon_master import DungeonMaster
from src.routes import game, generation

load_dotenv()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Initialize Dungeon Master
    app.state.dm = DungeonMaster(model=GEMINI_MODEL)
    yield
    # Cleanup if needed
    print("Closing AI Dungeon Master API...")


app = FastAPI(lifespan=lifespan)

app.include_router(game.router)
app.include_router(generation.router)


@app.get("/")
async def root():
    return {"Hello": "AI Dungeon Master API"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
