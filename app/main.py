from app.config import URL, REDIS_URL
from app.events.router import router as router_events
from app.members.router import router as router_members
from app.invite.router import router as router_invite
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from fastapi.staticfiles import StaticFiles
from redis import asyncio as aioredis


origins = [URL]
app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"))
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