import uvicorn
from fastapi import FastAPI

from dotenv import load_dotenv
from src.routes import generate

# GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

#
# @asynccontextmanager
# async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
#     # Initialize Dungeon Master
#     app.state.dm = DungeonMaster(model=GEMINI_MODEL)
#     yield
#     # Cleanup if needed
#     print("Closing AI Dungeon Master API...")
#

app = FastAPI()

app.include_router(generate.router)


@app.get("/")
async def root():
    return {"Hello": "AI Dungeon Master API"}


if __name__ == "__main__":
    load_dotenv()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
