import asyncio

import aiosqlite

DATABASE_URL = "database.db"

async def init_db():
    async with aiosqlite.connect(DATABASE_URL) as db:
        with open("migrations/schema.sql", "r") as f:
            await db.executescript(f.read())
        with open("migrations/data.sql", "r") as f:
            await db.executescript(f.read())
        await db.commit()

asyncio.run(init_db())
