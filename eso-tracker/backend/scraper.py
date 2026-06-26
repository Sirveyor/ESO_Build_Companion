"""UESP.net scraper for ESO gear set data."""
import re
import httpx
from bs4 import BeautifulSoup

UESP_BASE = "https://en.uesp.net"
UESP_WIKI = f"{UESP_BASE}/wiki"
UESP_API  = f"{UESP_BASE}/w/api.php"

_SET_TYPE_PATTERNS = [
    (r"\boverland\b", "overland"),
    (r"\bdungeon\b",  "dungeon"),
    (r"\btrial\b",    "trial"),
    (r"\bcrafted?\b", "crafted"),
    (r"\bpvp\b|\balliance war\b|\bcyrodiil\b|\bbattleground", "pvp"),
    (r"\bmonster\b",  "monster"),
    (r"\bmythic\b",   "mythic"),
    (r"\barena\b",    "arena"),
]

_HEADERS = {
    "User-Agent": "ESO-Build-Companion/1.0 (personal LAN app; contact: sirveyor.code@gmail.com)"
}


async def search_sets(query: str) -> list[dict]:
    """Search UESP for ESO set pages. Returns list of {name, url, snippet}."""
    params = {
        "action": "query",
        "list": "search",
        "srsearch": f"Online:{query}",
        "format": "json",
        "srlimit": "10",
    }
    async with httpx.AsyncClient(timeout=15, headers=_HEADERS) as client:
        r = await client.get(UESP_API, params=params)
        r.raise_for_status()
        data = r.json()

    results = []
    for item in data.get("query", {}).get("search", []):
        title = item["title"]
        if not title.startswith("Online:"):
            continue
        name = title[len("Online:"):]
        snippet = BeautifulSoup(item.get("snippet", ""), "html.parser").get_text()
        results.append({
            "name": name,
            "url": f"{UESP_WIKI}/{title.replace(' ', '_')}",
            "snippet": snippet[:120],
        })
    return results


async def scrape_set(url: str) -> dict:
    """Fetch a UESP set page and return parsed set data.

    Returns:
        {name, set_type, location, num_pieces, patch_version, bonuses: [{pieces_required, bonus_description}]}
    """
    async with httpx.AsyncClient(timeout=15, follow_redirects=True, headers=_HEADERS) as client:
        r = await client.get(url)
        r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    # --- Name ---
    title_el = soup.find("h1", id="firstHeading")
    raw_name = title_el.get_text(strip=True) if title_el else ""
    name = raw_name[len("Online:"):] if raw_name.startswith("Online:") else raw_name

    content = soup.find(class_="mw-parser-output")
    if not content:
        return {"name": name, "set_type": None, "location": None,
                "num_pieces": 5, "bonuses": [], "patch_version": None}

    # --- First paragraph: type + location ---
    first_p = content.find("p")
    # Use separator=" " so adjacent inline elements keep their spaces
    intro = first_p.get_text(separator=" ", strip=True).lower() if first_p else ""

    # Check intro text, then fall back to URL path for hints
    set_type = None
    for pattern, stype in _SET_TYPE_PATTERNS:
        if re.search(pattern, intro, re.IGNORECASE):
            set_type = stype
            break
    if not set_type:
        for pattern, stype in _SET_TYPE_PATTERNS:
            if re.search(pattern, url, re.IGNORECASE):
                set_type = stype
                break

    location = None
    loc_match = re.search(
        r"(?:drops?\s+in|found\s+in|located\s+in|available\s+in)\s+([A-Z][^.]+?)(?:\.|,|\s+and\b|\s+it\b)",
        first_p.get_text(separator=" ") if first_p else "",
    )
    if loc_match:
        location = loc_match.group(1).strip()
    # Fallback: look for a wiki link in the first paragraph pointing to a zone
    if not location and first_p:
        for a in first_p.find_all("a"):
            href = a.get("href", "")
            if "/wiki/Online:" in href and "Sets" not in href and "Style" not in href:
                location = a.get_text(strip=True)
                break

    # --- Bonuses section ---
    bonuses = []
    bonus_heading = content.find("span", id="Bonuses")
    if bonus_heading:
        bonus_p = bonus_heading.find_parent().find_next_sibling("p")
        if bonus_p:
            # Each line: "<b>N items</b>: description" or "N items: description"
            html_lines = str(bonus_p).split("<br")
            for line in html_lines:
                line_soup = BeautifulSoup(line, "html.parser")
                # separator=" " preserves spaces between adjacent inline tags
                text = line_soup.get_text(separator=" ", strip=True)
                # re.search (not re.match) because partial html fragments may have
                # leading junk like "/>" from the split
                m = re.search(r"(\d)\s+items?\s*[:\-–]\s*(.+)", text, re.IGNORECASE)
                if m:
                    pieces = int(m.group(1))
                    desc = m.group(2).strip()
                    # Normalise scaled values like "25-1096" → keep the max (CP160) value
                    desc = re.sub(r"\b\d+-(\d+)\b", r"\1", desc)
                    # Collapse multiple spaces introduced by separator=" "
                    desc = re.sub(r" {2,}", " ", desc)
                    bonuses.append({
                        "pieces_required": pieces,
                        "bonus_description": desc,
                    })

    num_pieces = max((b["pieces_required"] for b in bonuses), default=5)

    # Mythic items have exactly 1 piece and a single bonus — infer type if still unknown
    if not set_type and num_pieces == 1 and len(bonuses) == 1:
        set_type = "mythic"

    return {
        "name": name,
        "set_type": set_type,
        "location": location,
        "num_pieces": num_pieces,
        "patch_version": None,
        "bonuses": bonuses,
    }
