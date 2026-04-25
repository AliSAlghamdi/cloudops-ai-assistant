# CloudOps AI Assistant

A local MVP that combines:

- Cloud Q&A using an external LLM API
- Ticket classification using a local ML model
- Docker containerization
- Kubernetes local deployment on Docker Desktop

---

## Features

- Web UI for asking cloud questions
- Web UI for classifying support tickets
- `/ask` endpoint powered by an external LLM
- `/classify` endpoint powered by a trained ML model
- Docker support
- Kubernetes Deployment + Service + Secret
- Rolling update test on Kubernetes
- GitHub Actions CI workflow

---

## Project Structure

```text
CloudOpsAI/
├── app/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   ├── templates/
│   └── static/
├── data/
├── ml/
├── k8s/
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- FastAPI
- HTML / CSS
- Docker
- Kubernetes
- GitHub Actions
- OpenAI API
- scikit-learn

---

## Run Locally

### 1) Install dependencies

```bash
pip install -r requirements.txt
```

### 2) Set API key

On PowerShell:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

### 3) Run the app

```bash
python -m uvicorn app.main:app --reload
```

### 4) Open in browser

```text
http://127.0.0.1:8000
```

---

## Run with Docker

### Build image

```bash
docker build -t cloudops-ai-assistant .
```

### Run container

```powershell
docker run -d -p 8000:8000 --name cloudops-ai-assistant -e OPENAI_API_KEY="$env:OPENAI_API_KEY" cloudops-ai-assistant
```

---

## Run with Kubernetes (Docker Desktop)

### Create secret

```powershell
kubectl create secret generic openai-api-secret --from-literal=OPENAI_API_KEY="$env:OPENAI_API_KEY"
```

### Apply deployment and service

```powershell
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Port forward

```powershell
kubectl port-forward service/cloudops-ai-assistant-service 8001:80
```

### Open in browser

```text
http://127.0.0.1:8001
```

---

## API Endpoints

- `/health`
- `/ask`
- `/classify`

### Examples

```text
http://127.0.0.1:8000/ask?question=What%20is%20Cloud%20NAT
http://127.0.0.1:8000/classify?ticket=My%20password%20is%20not%20working
```

---

## Kubernetes Concepts Used

- **Pod**: runs the application container
- **Deployment**: manages Pods and keeps replicas alive
- **Service**: provides stable access to Pods
- **Secret**: stores the API key securely
- **Rolling Update**: updates Pods gradually without full downtime

---

## What I Practiced in This Project

- Building a FastAPI application
- Integrating an external LLM API
- Training and using a local ML classifier
- Containerizing the app with Docker
- Running the app in Kubernetes locally
- Using GitHub Actions for CI
- Performing a rolling update in Kubernetes

---

## Notes

- The OpenAI API key is **not stored in the code**
- The key is passed using **environment variables**
- The ML model is stored locally in the `ml/` folder

---

## Author

Ali Alghamdi