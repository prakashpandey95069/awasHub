import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os

# 1. Dataset path handle karein
csv_path = os.path.join("..", "data", "housing.csv")
if not os.path.exists(csv_path):
    csv_path = "housing.csv"

df = pd.read_csv(csv_path)

# 2. Target variable (Price)
df['price_lakhs'] = df['price'] / 100000

# 3. EXACT 5 FEATURES (Jo aapke UI me hain)
# area, bedrooms, bathrooms, stories, parking
X = df[['area', 'bedrooms', 'bathrooms', 'stories', 'parking']]
y = df['price_lakhs']

# 4. Model Training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Model ko 'src' aur 'model' dono folders me save karein taaki path issue na ho
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Agar 'model' folder exist karta hai toh wahan bhi copy save karein
model_folder = os.path.join("..", "model")
if os.path.exists(model_folder):
    with open(os.path.join(model_folder, 'model.pkl'), 'wb') as f:
        pickle.dump(model, f)

print("✅ Success: Model trained with 5 features and saved!")