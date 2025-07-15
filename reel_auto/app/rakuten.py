import requests, os, typing
from .config import RAKUTEN_APP_ID, RAKUTEN_AFF_ID, GENRE_ID

def get_items(top_n: int = 30, min_rate: float = 3.0) -> typing.List[dict]:
    """Return list of items sorted by affiliateRate desc."""
    params = {
        "applicationId": RAKUTEN_APP_ID,
        "affiliateId": RAKUTEN_AFF_ID,
        "genreId": GENRE_ID,
        "sort": "+affiliateRate",
        "hits": top_n,
        "format": "json"
    }
    r = requests.get(
        "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601",
        params=params, timeout=10
    )
    r.raise_for_status()
    items = r.json().get("Items", [])
    return [
        {
            "name": it["Item"]["itemName"][:60],
            "img": it["Item"]["mediumImageUrls"][0]["imageUrl"].split('?')[0],
            "url": it["Item"]["affiliateUrl"],
            "rate": float(it["Item"]["affiliateRate"])
        }
        for it in items
        if float(it["Item"]["affiliateRate"]) >= min_rate
    ]
