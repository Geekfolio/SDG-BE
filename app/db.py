import aiosqlite

DATABASE_URL = "../database.db"

async def init_db():
    async with aiosqlite.connect(DATABASE_URL) as db:
        with open("migrations/schema.sql", "r") as f:
            await db.executescript(f.read())
        with open("migrations/data.sql", "r") as f:
            await db.executescript(f.read())
        await db.commit()

async def execute_query(query, params=()):
    async with aiosqlite.connect(DATABASE_URL) as db:
        await db.execute(query, params)
        await db.commit()

async def fetch_all(query, params=()):
    async with aiosqlite.connect(DATABASE_URL) as db:
        cursor = await db.execute(query, params)
        rows = await cursor.fetchall()
        return rows
