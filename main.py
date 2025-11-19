
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd
import xgboost as xgb

MODEL_FEATURE_ORDER = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'scaled_amount', 'scaled_time']


app = FastAPI(title="Credit Card Fraud Detection API")

# Load XGBoost model
bst = xgb.Booster()
bst.load_model("models/XGBoost_best_model.json")

class Transaction(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    scaled_amount: float
    scaled_time: float


class BatchTransactions(BaseModel):
    transactions: List[Transaction]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(tx: Transaction):
    df = pd.DataFrame([tx.dict()])
    df = df[MODEL_FEATURE_ORDER]
    dmat = xgb.DMatrix(df)
    proba = float(bst.predict(dmat)[0])
    return {"xgb_proba": proba}

@app.post("/predict_batch")
def predict_batch(batch: BatchTransactions):
    df = pd.DataFrame([t.dict() for t in batch.transactions])
    df = df[MODEL_FEATURE_ORDER]
    dmat = xgb.DMatrix(df)
    probas = bst.predict(dmat).tolist()
    preds = [{"xgb_proba": float(p)} for p in probas]
    return {"predictions": preds}
