from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)

model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'model', 'model.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array([[
            float(data['area']),
            float(data['bedrooms']),
            float(data['bathrooms']),
            float(data['stories']),
            float(data['parking'])
        ]])
        prediction = model.predict(features)
        return jsonify({'price': round(prediction[0], 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    print("🚀 Flask Server starting on port 5001...")
    app.run(port=5001, debug=True)