# 🇮🇳 Indian House Price Predictor

A complete Machine Learning web application that predicts house prices in India based on key property characteristics. The project features a **Flask ML Service**, a **Node.js REST API**, and a modern, responsive **Frontend**.

---

## 🏗️ Project Architecture

The system is split into three main layers:
1. **Machine Learning Service (Python/Flask)**: Trains and serves the regression model.
2. **Backend Server (Node.js/Express)**: Acts as a proxy and handles API requests.
3. **Frontend (HTML/CSS/JS)**: Provides an interactive UI for entering data and displaying price estimates.

---

## 📁 Folder Structure

```text
house Price Prediction/
├── backend/
│   ├── node_modules/
│   ├── src/
│   │   └── app.js           # Node.js server (Port 5000)
│   ├── package.json
│   └── package-lock.json
├── data/
│   └── housing.csv          # Training dataset
├── frontend/
│   └── index.html           # UI with Sample Data & Clear features
└── ml-service/
    ├── model/
    │   └── model.pkl        # Serialized ML model
    └── src/
        ├── app.py           # Flask server (Port 5001)
        └── train.py         # Training script (5 features)