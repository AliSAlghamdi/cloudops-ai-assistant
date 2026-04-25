from app.services.llm_service import ask_llm


def get_answer(question: str) -> str:
    if not question.strip():
        return "Please enter a question."

    return ask_llm(question)