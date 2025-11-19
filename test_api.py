import requests
import json

# API base URL
BASE_URL = "http://localhost:8080"

# -----------------------------
# 1️⃣ Test single transaction
# -----------------------------
with open("transaction.json", "r") as f:
    transaction_data = json.load(f)

response = requests.post(f"{BASE_URL}/predict", json=transaction_data)
print("Single transaction prediction:")
print(response.json())

# -----------------------------
# 2️⃣ Test batch transactions
# -----------------------------
with open("batch_transactions.json", "r") as f:
    batch_data = json.load(f)

response = requests.post(f"{BASE_URL}/predict_batch", json=batch_data)
print("\nBatch transactions predictions:")
print(response.json())
