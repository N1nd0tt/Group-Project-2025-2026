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
            await conn.execute(query, campaign.campaign_id, campaign.owner_id, campaign.setting_id, campaign.name)
            
            # Automatically add an owner player to campaign
            player_query = """
            INSERT INTO campaign_players (campaign_id, player_id)
            VALUES ($1, $2)
            """
            await conn.execute(player_query, campaign.campaign_id, campaign.owner_id)

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

    async def update_campaign(self, campaign: Campaign):
        query = """
        UPDATE campaigns
        SET owner_id = $1, setting_id = $2, name = $3
        WHERE campaign_id = $4
        """
        await self.pool.execute(query, campaign.owner_id, campaign.setting_id, campaign.name, campaign.campaign_id)

    async def add_player_to_campaign(self, campaign_id: str, player_id: str):
        query = """
        INSERT INTO campaign_players (campaign_id, player_id)
        VALUES ($1, $2)
        """
        await self.pool.execute(query, campaign_id, player_id)

    async def delete_campaign(self, campaign_id: str):
        campaign = await self.get_campaign(campaign_id)
        if campaign:
            history_query = """
            INSERT INTO histories (campaign_id, owner_id, status, details)
            VALUES ($1, $2, $3, $4)
            """
            await self.pool.execute(history_query, campaign.campaign_id, campaign.owner_id, "deleted", f"Campaign {campaign.name} was deleted")

        # First remove related players, then the campaign
        await self.pool.execute("DELETE FROM campaign_players WHERE campaign_id = $1", campaign_id)
        
        query = """
        DELETE FROM campaigns
        WHERE campaign_id = $1
        """
        await self.pool.execute(query, campaign_id)

class ChatMessagesDB:
    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool

    async def get_messages(self, campaign_id: str) -> list[dict]:
        query = """
        SELECT sender, content
        FROM chat_messages
        WHERE campaign_id = $1
        ORDER BY created_at ASC
        """
        async with self.pool.acquire() as conn:
            rows = await conn.fetch(query, campaign_id)
            return [{"sender": row["sender"], "content": row["content"]} for row in rows]

    async def add_message(self, campaign_id: str, sender: str, content: str):
        query = """
        INSERT INTO chat_messages (campaign_id, sender, content)
        VALUES ($1, $2, $3)
        """
        await self.pool.execute(query, campaign_id, sender, content)

