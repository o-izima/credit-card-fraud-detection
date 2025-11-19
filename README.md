# Credit Card Fraud Detection

A machine learning project that detects fraudulent credit card transactions using XGBoost. The project provides both a Jupyter notebook for EDA, preprocessing, and model training, as well as a FastAPI-based REST API and Docker deployment for serving predictions.  

---

## Table of Contents

- [Project Structure](#project-structure)  
- [Features](#features)  
- [Requirements](#requirements)  
- [Technologies](#technologies)  
- [Setup & Installation](#setup--installation)  
- [Running the API](#running-the-api)  
- [Testing the API](#testing-the-api)  
- [Docker](#docker)  
- [License](#license)  

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


