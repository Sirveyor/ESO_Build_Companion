from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import characters, builds, gear, skills, traits, sources, users, gear_sets, reference, recipes, motifs, fragments
from init_db import init_db

_VERSION_FILE = Path(__file__).parent.parent / "VERSION"

app = FastAPI(title="ESO Build Tracker API", version="0.1.0")

# Allow the Svelte dev server and any LAN device to reach the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

@app.get("/version")
def get_version():
    try:
        return {"version": _VERSION_FILE.read_text().strip()}
    except FileNotFoundError:
        return {"version": "unknown"}

app.include_router(users.router)
app.include_router(characters.router)
app.include_router(builds.router)
app.include_router(gear.router)
app.include_router(gear_sets.router)
app.include_router(skills.router)
app.include_router(traits.router)
app.include_router(sources.router)
app.include_router(reference.router)
app.include_router(recipes.router)
app.include_router(motifs.router)
app.include_router(fragments.router)
