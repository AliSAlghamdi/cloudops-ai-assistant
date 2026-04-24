from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.qa_service import get_answer
from app.services.classify_service import classify_ticket

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request, question: str = "", ticket: str = ""):
    answer = get_answer(question) if question else None
    category = classify_ticket(ticket) if ticket else None

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "question": question,
            "ticket": ticket,
            "answer": answer,
            "category": category,
        },
    )