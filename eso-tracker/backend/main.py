from fastapi import FastAPI
from routers import characters, builds, gear, skills, traits, sources, users, gear_sets
from init_db import init_db

app = FastAPI(title="ESO Build Tracker API", version="0.1.0")

init_db()

app.include_router(users.router)
app.include_router(characters.router)
app.include_router(builds.router)
app.include_router(gear.router)
app.include_router(gear_sets.router)
app.include_router(skills.router)
app.include_router(traits.router)
app.include_router(sources.router)
