import unicodedata
from fastapi import HTTPException
from models.transport_service import TransportService
import re

CITY_ALIASES = {
    "washington d c": "washington dc",
    "washington dc": "washington dc",
    "new york": "new york",
    "san francisco": "san francisco",
    "los angeles": "los angeles",
}

routes = {
    ("new york", "washington dc"): [
        TransportService(company = "Knight-Swift Transport Services", trucks_per_day = 10),
        TransportService(company = "J.B. Hunt Transport Services Inc", trucks_per_day = 7),
        TransportService(company = "YRC Worldwide", trucks_per_day = 5),
    ],
    ("san francisco", "los angeles"): [
        TransportService(company = "XPO Logistics", trucks_per_day = 9),
        TransportService(company = "Schneider", trucks_per_day = 6),
        TransportService(company = "Landstar Systems", trucks_per_day = 2),
    ]
}

def normalize_city_name(city: str) -> str:
    # Replace multiple spaces with a single space
    city = re.sub(r"\s+", " ", city.strip())
    # Remove unnecessary punctuation (optional)
    city = city.replace(".", "", -1).lower()
    # Remove non-ASCII characters
    city = unicodedata.normalize("NFKD", city).encode("ascii", "ignore").decode("utf-8")
    # Check for aliases and return the standardized name
    return CITY_ALIASES.get(city, city)

default_services = [
    TransportService(company = "UPS Inc.", trucks_per_day = 11),
    TransportService(company = "FedEx Corp", trucks_per_day = 9),
]

def get_transport_services(from_city: str, to_city: str):
    from_city = normalize_city_name(from_city)
    to_city = normalize_city_name(to_city)

    print(f"Getting transport services from {from_city} to {to_city}")
    key = (from_city, to_city)
    if key in routes:
        return routes[key]
    elif to_city in ["washington dc", "los angeles"]:
        return default_services
    else:
        raise HTTPException(status_code=404, detail="No transport services found")
    
    
