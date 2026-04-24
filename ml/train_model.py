from pathlib import Path
import csv
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "tickets.csv"
MODEL_FILE = BASE_DIR / "ml" / "ticket_classifier.joblib"


def load_training_data():
    texts = []
    labels = []

    with DATA_FILE.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            texts.append(row["ticket"])
            labels.append(row["category"])

    return texts, labels


def main():
    texts, labels = load_training_data()

    model = Pipeline(
        steps=[
            ("tfidf", TfidfVectorizer()),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )

    model.fit(texts, labels)

    accuracy = model.score(texts, labels)

    joblib.dump(model, MODEL_FILE)

    print(f"Model trained successfully.")
    print(f"Training accuracy: {accuracy:.2f}")
    print(f"Saved to: {MODEL_FILE}")


if __name__ == "__main__":
    main()