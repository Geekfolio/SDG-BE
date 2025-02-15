from robyn import Robyn
from routes import user_router

app = Robyn(__file__)

# registering routes
app.include_router(user_router)

@app.get("/")
async def index():
    return "za-warudo"

if __name__ == "__main__":
    app.start(host="0.0.0.0", port=8080)
