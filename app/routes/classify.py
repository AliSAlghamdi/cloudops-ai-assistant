from fastapi import APIRouter
from app.services.classify_service import classify_ticket

router = APIRouter()


@router.get("/classify")
def classify(ticket: str):
    category = classify_ticket(ticket)

    return {
        "ticket_received": ticket,
        "category": category
    }