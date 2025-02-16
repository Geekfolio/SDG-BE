from robyn import ALLOW_CORS, Robyn
from routes import events_router, user_router

app = Robyn(__file__)
ALLOW_CORS(app, "*")

# registering routes
app.include_router(user_router)
app.include_router(events_router)

@app.get("/")
async def index():
    return "za-warudo"

if __name__ == "__main__":
    app.start(host="0.0.0.0", port=8080)
