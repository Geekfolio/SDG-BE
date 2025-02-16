import controllers.user as user_controllers
from robyn import SubRouter

user_router = SubRouter(__file__, prefix="/user")

@user_router.post("/register")
async def create_user_route(request):
    return await user_controllers.create_user(request)

@user_router.get("/fetch")
async def fetch_user_route(request):
    return await user_controllers.fetch_user(request)

@user_router.get("/all")
async def fetch_all_users_route(request):
    return await user_controllers.fetch_all_users(request)

@user_router.post("/login")
async def login_route(request):
    return await user_controllers.login(request)