from fastapi import APIRouter
from models.transport_service import TransportService
from services.transport_service import get_transport_services

router = APIRouter()

@router.get("/get-transport-services/", response_model=list[TransportService])
async def get_transport_services_endpoint(from_city: str, to_city: str):
    return get_transport_services(from_city, to_city)
