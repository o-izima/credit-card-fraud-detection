# Credit Card Fraud Detection - End-to-End ML Pipeline with FastAPI & Docker Model Deployment

A machine learning project that detects fraudulent credit card transactions using XGBoost, the best performing model. The project provides both a Jupyter notebook for EDA, preprocessing, and model training, as well as a FastAPI-based REST API and Docker deployment for serving predictions.  

---

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure) 
- [Business Objective](#business-objective)
- [Dataset](#dataset)
- [Data Preparation](#data-prep)
- [Modeling Approach](#modeling) 
- [Model Evaluation](#model-eval)
- [Requirements](#requirements)  
- [Technologies](#technologies)  
- [Setup & Installation](#setup--installation)  
- [Running the API](#running-the-api)  
- [Testing the API](#testing-the-api)  
- [Docker](#docker)  
- [License](#license)  

---
## 1. Project Overview
Credit card fraud leads to significant financial losses for banks and customers.
This project builds a complete machine learning system capable of:
- Detecting fraudulent transactions using classification models.
- Producing probability-based fraud risk scores.
- Deploying the best-performing model as a REST API using FastAPI and Docker.
The project covers the full ML lifecycle—from EDA and preprocessing to model selection, hyperparameter tuning, and deployment.

---
## 2. Project Structure

```text
.
├── Dockerfile                      # Dockerfile for containerizing the API
├── README.md                       # Project documentation
├── requirements.txt                # Python dependencies
├── cleanup_repo.sh                 # Optional script to clean repository files
├── generate_dockerfile.py          # Optional utility script for Dockerfile generation
├── creditcard_fraud_detection.ipynb # Jupyter notebook for EDA, preprocessing, and model training
├── main.py                         # FastAPI application
├── test_api.py                     # Python script for testing API predictions
├── transaction.json                # Example single transaction input
├── batch_transactions.json         # Example batch transactions input
└── models                          # Saved trained model(s)
```
---
## 3. Business Objective
### Problem Statement
Financial institutions require an automated fraud detection system that can identify suspicious transactions while reducing false positives.

### Goal
Predict whether a given credit card transaction is fraudulent or legitimate using machine learning.

The deployed XGBoost algorithm is setup as a standard binary classification model for fraud detection:
- The model usually outputs a probability (proba) between 0 and 1 representing the likelihood that a transaction is fraudulent.
- The **typical threshold is 0.5**:
    - `proba >= 0.5` → predicted fraudulent
    - `proba < 0.5` → predicted legitimate / not fraud

So if your prediction is less than 0.5, it is considered not fraud.

⚠️ Note: Sometimes, for imbalanced datasets like credit card fraud, it’s common to lower the threshold (e.g., 0.3) to catch more fraud cases, trading off some false positives for higher recall.

### Impact
- Reduces financial losses.
- Improves detection efficiency.
- Helps fraud investigators prioritize high-risk transactions.

---

## 4. Dataset
### Source

Kaggle: [Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

### Description
- 284,807 transactions over two days.
- Only 492 fraud cases (~0.172%) → highly imbalanced dataset.
- Features:
    - V1–V28: PCA-transformed numeric components
    - Amount: Transaction amount
    - Time: Time difference between transactions    
    - Class: Target → 0 = legitimate, 1 = fraud

### Why this dataset works
- Publicly available and clean.
- Severe class imbalance supports learning specialized evaluation strategies.
- Suitable for comparing multiple ML algorithms.
---
## 5. Data Preparation
### Exploratory Data Analysis (EDA)
- Examine class imbalance
- Visualize distributions
- Inspect relationships between Amount, Time, and fraud frequency

### Preprocessing
- Standardize Amount and Time
- Manage class imbalance (class_weight, undersampling, or SMOTE)
- Train/validation/test split

---
## 6. Modeling Approach

### Models Trained
1. Logistic Regression (LR)
2. Random Forest (RF)
3. XGBoost

### Performance Summary
- Default settings:
    → Random Forest performed the best.
- After Optuna hyperparameter tuning and evaluation on holdout test data:
    → XGBoost was the best-performing model, followed by Random Forest.

### Deployment Choice
- **XGBoost** selected and deployed as the final production model.
---

## 7. Model Evaluation
Given the highly imbalanced nature of the dataset (fraud cases ≈ 0.17%), traditional accuracy is not meaningful. Instead, the following evaluation metrics were used:
- **PR-AUC (Precision–Recall AUC)** - Primary Metric
     → PR-AUC is better for extreme class imbalance (focuses on detecting fraud)
     → Properly penalizes false positives and false negatives.
- ROC-AUC
     → Useful for model comparison but less sensitive to class imbalance, as true negatives dominate.
- Classification Report
- Cross Validation
- Holdout test set evaluation
---

## 8. Deployment Workflow
### Model Serialization
- Saved using joblib or pickle.

### API Development
- Implemented using FastAPI
- Endpoints support:
    - Single transaction prediction
    - Batch predictions

### Containerization
- Dockerfile created for reproducible builds.
- Image runs the FastAPI service for real-time prediction

### Execution
- Local or cloud deployment possible using Docker commands.

---

## 9. Requirements
- Python 3.10+
- Pip 

Install required Python packages: 
```text
pip install -r requirements.txt
```
---

## 10. Technologies
- Python
- XGBoost, RF & LR
- Pandas & NumPy
- Scikit-learn
- FastAPI
- Uvicorn
- Docker
---

## 11. Setup & Installation
Clone the repository:
```text
git clone <repo_url>
cd credit-card-fraud-detection
```
Install dependencies
```text
pip install -r requirements.txt
```
Ensure your models/ folder contains the trained model (generated from the notebook).


---
## 12. Running the API
Start the FastAPI application:
```text
python main.py
```
By default, the API runs at:
```text
http://localhost:8080
```
Available endpoints:
- POST /predict – Predict a single transaction
- POST /predict_batch – Predict multiple transactions
- GET /health – Health check
---

## 13. Testing the API
Use `test_api.py` to test predictions with sample JSON files:
```text
python test_api.py
```
Example files:
- `transaction.json` – Single transaction
- `batch_transactions.json` – Batch transactions
The script will print the predicted probability of fraud.
---
## 14. Docker
Build the Docker image:
```text
docker build -t fraud-api .
```
Run the Docker container:
```text
docker run -p 8080:8080 fraud-api
```

Test the API inside the container using the same test_api.py script or curl.

---

## 15. License

This project is licensed under the MIT License.  

You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, provided that the original copyright notice and this permission notice are included in all copies or substantial portions of the software.  

