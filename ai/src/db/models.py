import json

import asyncpg

from src.models.campaign import Campaign
from src.models.setting import Setting


class SettingsDB:
    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool

    async def create_setting(self, setting_id: str, setting: Setting):
        query = """
                INSERT INTO settings (setting_id, data)
                VALUES ($1, $2)
                """

        async with self.pool.acquire() as conn:
            await conn.execute(query, setting_id, setting.model_dump_json())

    async def get_setting(self, setting_id: str) -> Setting | None:
        query = """
                SELECT data
                FROM settings
                WHERE setting_id = $1
                """

        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(query, setting_id)
            if row:
                setting_data = row['data']
                return Setting.model_validate_json(setting_data)
            else:
                return None


class CampaignsDB:
    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool

    async def create_campaign(self, campaign: Campaign):
        query = """
                INSERT INTO campaigns (campaign_id, owner_id, setting_id, name)
                VALUES ($1, $2, $3, $4)
                """

        async with self.pool.acquire() as conn:
            await conn.execute(query, campaign.id, campaign.owner_id, campaign.setting_id, campaign.name)

    async def get_campaign(self, campaign_id: str) -> Campaign | None:
        query = """
                SELECT *
                FROM campaigns
                WHERE campaign_id = $1
                """

        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(query, campaign_id)
            if row:
                return Campaign.model_validate(dict(row))
            else:
                return None
