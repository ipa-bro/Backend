from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from itsdangerous import URLSafeSerializer
from asyncio import sleep
from app.config import SECRET_KEY, USERNAME, PASSWORD


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]
        if validate_credentials(username, password):
            token = URLSafeSerializer(SECRET_KEY).dumps({"username": username})
            request.session.update({"token": token})
            return True
        else:
            await sleep(3)
            return False


    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True


    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        if not token:
            return False
        try:
            data = URLSafeSerializer(SECRET_KEY).loads(token)
            username = data.get("username")
            if username:
                return True
            else:
                return False
        except Exception as e:
            return False


def validate_credentials(username: str, password: str) -> bool:
    if username == USERNAME and password == PASSWORD:
        return True
    else:
        return False


authentication_backend = AdminAuth(secret_key=SECRET_KEY)

