import unicodedata
from fastapi import HTTPException
from models.transport_service import TransportService

routes = {
    ("new york", "washington d c"): [
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

default_services = [
    TransportService(company = "UPS Inc.", trucks_per_day = 11),
    TransportService(company = "FedEx Corp", trucks_per_day = 9),
]

def get_transport_services(from_city: str, to_city: str):
    from_city = from_city.lower().replace(".", "")
    to_city = to_city.lower().replace(".", "")

    normalizedFromCity = unicodedata.normalize("NFKD", from_city).encode("ascii", "ignore").decode("utf-8")
    normalizedToCity = unicodedata.normalize("NFKD", to_city).encode("ascii", "ignore").decode("utf-8")

    key = (normalizedFromCity, normalizedToCity)
    if key in routes:
        return routes[key]
    elif normalizedToCity in ["washington d c", "los angeles"]:
        return default_services
    else:
        raise HTTPException(status_code=404, detail="No transport services found")
    
    
