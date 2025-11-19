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
- [Requirements](#requirements)  
- [Technologies](#technologies)  
- [Setup & Installation](#setup--installation)  
- [Running the API](#running-the-api)  
- [Testing the API](#testing-the-api)  
- [Docker](#docker)  
- [License](#license)  

---
## Project Overview
Credit card fraud leads to significant financial losses for banks and customers.
This project builds a complete machine learning system capable of:
- Detecting fraudulent transactions using classification models.
- Producing probability-based fraud risk scores.
- Deploying the best-performing model as a REST API using FastAPI and Docker.
The project covers the full ML lifecycle—from EDA and preprocessing to model selection, hyperparameter tuning, and deployment.

---
## Project Structure

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
## 3. Business Objective
### Problem Statement
Financial institutions require an automated fraud detection system that can identify suspicious transactions while reducing false positives.

### Goal
Predict whether a given credit card transaction is fraudulent or legitimate using machine learning.

### Impact
- Reduces financial losses.
- Improves detection efficiency.
- Helps fraud investigators prioritize high-risk transactions.

## Dataset

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

## Data Preparation
### Exploratory Data Analysis (EDA)
- Examine class imbalance
- Visualize distributions
- Inspect relationships between Amount, Time, and fraud frequency

### Preprocessing
- Standardize Amount and Time
- Manage class imbalance (class_weight, undersampling, or SMOTE)
- Train/validation/test split

## Modeling Approach

### Models Trained
1. Logistic Regression
2. Random Forest
3. XGBoost

### Performance Summary
- Default settings:
    → Random Forest performed the best.
- After Optuna hyperparameter tuning and evaluation on holdout test data:
    → XGBoost was the best-performing model, followed by Random Forest.

### Deployment Choice
- **XGBoost** selected and deployed as the final production model.