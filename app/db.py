import aiosqlite

DATABASE_URL = "database.db"

async def execute_query(query, params=(), fetch_last_id = False):
    async with aiosqlite.connect(DATABASE_URL) as db:
        cursor = await db.execute(query, params)
        last_id = cursor.lastrowid if fetch_last_id else None
        await db.commit()
        await cursor.close()
        return last_id

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

async def execute_many(query, params_list, fetch_last_id=False):
    async with aiosqlite.connect(DATABASE_URL) as db:
        cursor = await db.executemany(query, params_list)
        last_id = cursor.lastrowid if fetch_last_id else None
        await db.commit()
        await cursor.close()
        return last_id
