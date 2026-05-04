# 🇮🇳 AwasHub: Indian House Price Predictor

A complete full-stack Machine Learning web application that predicts house prices in India based on key property characteristics. The project features a **Flask ML Service**, a **Node.js REST API**, and a modern, responsive **Frontend Dashboard**.

---

## 🏗️ Project Architecture

The system is split into three main decoupled layers:

1. **Machine Learning Service (Python/Flask)**: Trains and serves the regression model.
2. **Backend Server (Node.js/Express)**: Acts as a proxy/gateway and handles API requests.
3. **Frontend (HTML/CSS/JS)**: Responsive Single Page Dashboard for entering data and displaying price estimates.

````text
[Frontend: HTML/CSS/JS]
       │
       ▼ (Fetch Request on Port 5000)
[Backend: Node.js / Express]
       │
       ▼ (Axios Call on Port 5001)
[ML Service: Flask API] ───> Uses [model.pkl] to predict ───> Returns Price
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




## 🚀 Setup and Installation

### 📋 Prerequisites
* **Python 3.10+**
* **Node.js 18+**

---

### 🛠️ Step 1: Setup ML Service
1. Navigate to the ML folder:
   ```bash
   cd ml-service

  Install dependencies:

Bash
pip install flask flask-cors pandas scikit-learn numpy
Train the model:

Bash
python src/train.py
Start the Flask server:

Bash
python src/app.py
Runs on http://127.0.0.1:5001

🌐 Step 2: Setup Backend Server
Open a new terminal and navigate to the backend folder:

Bash
cd backend
Install packages:

Bash
npm install express axios cors
Start the Node server:

Bash
node src/app.js
Runs on http://127.0.0.1:5000

💻 Step 3: Launch Frontend
Navigate to the frontend/ folder.

Open index.html directly in your browser.
````
