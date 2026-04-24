from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.qa import router as qa_router
from app.routes.classify import router as classify_router
from app.routes.web import router as web_router

app = FastAPI(title="CloudOps AI Assistant")

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "CloudOps AI Assistant"
    }


app.include_router(web_router)
app.include_router(qa_router)
app.include_router(classify_router)