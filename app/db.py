import aiosqlite

DATABASE_URL = "database.db"

async def execute_query(query, params=()):
    async with aiosqlite.connect(DATABASE_URL) as db:
        await db.execute(query, params)
        await db.commit()

async def fetch_all(query, params=()):
    async with aiosqlite.connect(DATABASE_URL) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute(query, params)
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]

async def fetch_one(query, params=()):
    async with aiosqlite.connect(DATABASE_URL) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute(query, params)
        row = await cursor.fetchone()
        return dict(row) if row else None

async def fetch_value(query, params=()):
    async with aiosqlite.connect(DATABASE_URL) as db:
        cursor = await db.execute(query, params)
        row = await cursor.fetchone()
        return row[0] if row else None

async def execute_many(query, params_list):
    async with aiosqlite.connect(DATABASE_URL) as db:
        await db.executemany(query, params_list)
        await db.commit()
