import uvicorn
from fastapi import FastAPI


from dotenv import load_dotenv
from src.routes import game, generation

load_dotenv()

app = FastAPI()

app.include_router(game.router)
app.include_router(generation.router)


@app.get("/")
async def root():
    return {"Hello": "AI Dungeon Master API"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
