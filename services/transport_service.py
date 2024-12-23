from models.transport_service import TransportService

routes = {
    ("New York", "Washington DC"): [
        TransportService(company = "Knight-Swift Transport Services", trucks_per_day = 10),
        TransportService(company = "J.B. Hunt Transport Services Inc", trucks_per_day = 7),
        TransportService(company = "YRC Worldwide", trucks_per_day = 5),
    ],
    ("San Francisco", "Los Angeles"): [
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
    key = (from_city, to_city)
    if key in routes:
        return routes[key]
    elif to_city in ["Washington DC", "Los Angeles"]:
        return default_services
    else:
        raise ValueError("No transport services available for the given route.")
