from sklearn.linear_model import LinearRegression
import pickle
from preprocess import load_data, preprocess

data = load_data()
X, y = preprocess(data)

model = LinearRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")