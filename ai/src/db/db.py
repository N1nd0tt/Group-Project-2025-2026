import asyncpg
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi import Request

DATABASE_URL = "db_url_example"


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with asyncpg.create_pool(
            dsn=DATABASE_URL,
            min_size=1,
            max_size=10) as pool:
        app.state.pool = pool
        async with pool.acquire() as conn:
            await conn.execute("""
            CREATE TABLE IF NOT EXISTS campaign_players (
                campaign_id VARCHAR(255) NOT NULL,
                player_id VARCHAR(255) NOT NULL,
                PRIMARY KEY (campaign_id, player_id)
            );
            
            CREATE TABLE IF NOT EXISTS chat_messages (
                id SERIAL PRIMARY KEY,
                campaign_id VARCHAR(255) NOT NULL,
                sender VARCHAR(50) NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            
            CREATE TABLE IF NOT EXISTS histories (
                id SERIAL PRIMARY KEY,
                campaign_id VARCHAR(255) NOT NULL,
                owner_id VARCHAR(255) NOT NULL,
                status VARCHAR(50) NOT NULL,
                details TEXT NOT NULL
            );
            """)

        yield


async def get_db_pool(request: Request) -> asyncpg.Pool:
    if not hasattr(request.app.state, "pool"):
        raise RuntimeError("Pool is not initialized")
    return request.app.state.pool
