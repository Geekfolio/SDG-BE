import aiosqlite
from db import init_db
from robyn import Robyn

app = Robyn(__file__)

@app.get("/")
async def index():
    await init_db()

if __name__ == "__main__":
    app.start(host="0.0.0.0", port=8080)
