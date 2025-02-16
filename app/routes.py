import controllers.events as event_controllers
import controllers.user as user_controllers
from robyn import SubRouter

user_router = SubRouter(__file__, prefix="/user")

@user_router.post("/register")
async def create_user_route(request):
    return await user_controllers.create_user(request)

@user_router.post("/fetch")
async def fetch_user_route(request):
    return await user_controllers.fetch_user(request)

@user_router.get("/all")
async def fetch_all_users_route(request):
    return await user_controllers.fetch_all_users(request)

@user_router.post("/login")
async def login_route(request):
    return await user_controllers.login(request)


events_router = SubRouter(__file__, prefix="/events")

@events_router.post("/create")
async def create_event_route(request):
    return await event_controllers.create_event(request)

@events_router.get("/all")
async def get_all_events_route(request):
    return await event_controllers.fetch_all_events(request)
