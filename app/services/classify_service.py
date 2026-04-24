from functools import lru_cache
from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent.parent
MODEL_FILE = BASE_DIR / "ml" / "ticket_classifier.joblib"


@lru_cache
def load_model():
    return joblib.load(MODEL_FILE)


def classify_ticket(ticket: str) -> str:
    if not MODEL_FILE.exists():
        return "Model not trained yet"

    model = load_model()
    prediction = model.predict([ticket])[0]
    return str(prediction)