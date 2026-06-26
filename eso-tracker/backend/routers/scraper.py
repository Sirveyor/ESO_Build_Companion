import uuid
import httpx
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from models.gear_set import GearSet, SetBonus
from schemas import GearSetSchema
import scraper as sc

router = APIRouter(prefix="/scraper", tags=["scraper"])


@router.get("/search")
async def search(q: str):
    """Search UESP for ESO set pages matching the query string."""
    if not q or len(q.strip()) < 2:
        raise HTTPException(status_code=400, detail="Query must be at least 2 characters")
    try:
        return await sc.search_sets(q.strip())
    except httpx.HTTPError as e:
        raise HTTPException(status_code=502, detail=f"UESP search failed: {e}")


@router.post("/preview")
async def preview(body: dict):
    """Fetch and parse a UESP set page without saving to the database.

    Body: {url: str}
    Returns the parsed set data for the user to review before importing.
    """
    url = (body.get("url") or "").strip()
    if not url or "uesp.net" not in url:
        raise HTTPException(status_code=400, detail="Provide a valid UESP URL")
    try:
        return await sc.scrape_set(url)
    except httpx.HTTPError as e:
        raise HTTPException(status_code=502, detail=f"Failed to fetch page: {e}")


@router.post("/import", response_model=GearSetSchema)
async def import_set(body: dict, db: Session = Depends(get_db)):
    """Scrape a UESP page and save the gear set + bonuses to the database.

    Body: {url: str, overwrite: bool = false}
    Returns the saved GearSetSchema.
    """
    url = (body.get("url") or "").strip()
    overwrite = bool(body.get("overwrite", False))
    if not url or "uesp.net" not in url:
        raise HTTPException(status_code=400, detail="Provide a valid UESP URL")

    try:
        data = await sc.scrape_set(url)
    except httpx.HTTPError as e:
        raise HTTPException(status_code=502, detail=f"Failed to fetch page: {e}")

    if not data.get("name"):
        raise HTTPException(status_code=422, detail="Could not parse set name from page")

    existing = db.query(GearSet).filter(GearSet.name == data["name"]).first()
    if existing and not overwrite:
        raise HTTPException(
            status_code=409,
            detail=f"Set '{data['name']}' already exists. Send overwrite=true to replace it."
        )

    if existing:
        for b in list(existing.bonuses):
            db.delete(b)
        existing.set_type     = data.get("set_type")
        existing.location     = data.get("location")
        existing.num_pieces   = data.get("num_pieces")
        existing.patch_version = data.get("patch_version")
        existing.last_updated = datetime.now(timezone.utc).isoformat()
        existing.notes        = f"Imported from {url}"
        gear_set = existing
    else:
        gear_set = GearSet(
            id            = str(uuid.uuid4()),
            name          = data["name"],
            set_type      = data.get("set_type"),
            location      = data.get("location"),
            num_pieces    = data.get("num_pieces"),
            patch_version = data.get("patch_version"),
            last_updated  = datetime.now(timezone.utc).isoformat(),
            notes         = f"Imported from {url}",
        )
        db.add(gear_set)

    db.flush()

    for b in data.get("bonuses", []):
        db.add(SetBonus(
            id                = str(uuid.uuid4()),
            set_id            = gear_set.id,
            pieces_required   = b["pieces_required"],
            bonus_description = b["bonus_description"],
        ))

    db.commit()
    db.refresh(gear_set)
    return gear_set
