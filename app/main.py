import time


from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin

from app.admin.views import EventsAdmin
from app.admin.auth import authentication_backend
from app.config import URL 
from app.database import engine
from app.events.router import router as router_events
from app.invite.router import router as router_invite


origins = ["*"]
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
app.include_router(router_events)
app.include_router(router_invite)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Set-Cookie", 
                   "Access-Control-Allow-Headers", 
                   "Access-Control-Allow-Origin", 
                   "Authorization"],
)



admin = Admin(app, engine, authentication_backend=authentication_backend)
admin.add_view(EventsAdmin)


