from fastapi import APIRouter
from app.services.qa_service import get_answer

router = APIRouter()


@router.get("/ask")
def ask(question: str):
    answer = get_answer(question)

    return {
        "question_received": question,
        "answer": answer
    }