
FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libgomp1 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app
COPY . /app

# Copy the XGBoost model from models folder into container
COPY models/XGBoost_best_model.json /app/models/XGBoost_best_model.json

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
