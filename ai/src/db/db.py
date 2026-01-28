import asyncpg
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi import Request

DATABASE_URL = "postgresql://admin:admin@localhost:5432/dnd_dm"


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with asyncpg.create_pool(
            dsn=DATABASE_URL,
            min_size=1,
            max_size=10) as pool:
        app.state.pool = pool

        yield


async def get_db_pool(request: Request) -> asyncpg.Pool:
    if not hasattr(request.app.state, "pool"):
        raise RuntimeError("Pool is not initialized")
    return request.app.state.pool
