from sqladmin import Admin
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse
from jose import jwt
from dotenv import load_dotenv
import os


class AdminAuth(AuthenticationBackend):

    secret_key = "secret_key"
    payload = "payload"


    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        load_dotenv()

        username_admin = os.getenv("USERNAME")
        password_admin = os.getenv("PASSWORD")

        if username_admin == username and password == password_admin:
            token = generate_token(self.payload, self.secret_key)
            request.session.update({"token": token})
            return True
        
        return False

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        try:
            jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return True
        except jwt.JWTError:
            return False

    
async def generate_token(payload, secret_key):
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        return token

authentication_backend = AdminAuth(secret_key="secret_key")
