from pydantic import BaseModel

class TransportService(BaseModel):
    company: str
    trucks_per_day: int
