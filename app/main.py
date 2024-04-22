import time

import sentry_sdk
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from sqladmin import Admin

from app.admin.views import EventsAdmin
from app.admin.auth import authentication_backend
from app.config import REDIS_URL, URL
from app.database import engine
from app.events.router import router as router_events
from app.invite.router import router as router_invite
from app.members.router import router as router_members
from app.logger import logger


origins = [URL]
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
app.include_router(router_events)
app.include_router(router_members)
app.include_router(router_invite)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS", "POST"],
    allow_headers=["Content-Type", "Set-Cookie", 
                   "Access-Control-Allow-Headers", 
                   "Access-Control-Allow-Origin", 
                   "Authorization"],
)


@app.on_event("startup")
def startup():
    redis = aioredis.from_url(REDIS_URL)
    FastAPICache.init(RedisBackend(redis), prefix="cache")


admin = Admin(app, engine, authentication_backend=authentication_backend)
admin.add_view(EventsAdmin)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info("Time", extra={
        "process_time": round(process_time, 2)
        })
    return response


sentry_sdk.init(
    dsn="https://975d74878cf39016c6af64d0380ecc93@o4507064479318016.ingest.us.sentry.io/4507064481873920",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
