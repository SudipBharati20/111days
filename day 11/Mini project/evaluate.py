from sklearn.metrics import mean_squared_error
import pickle
from preprocess import load_data, preprocess

data = load_data()
X, y = preprocess(data)

model = pickle.load(open("model.pkl", "rb"))
preds = model.predict(X)

mse = mean_squared_error(y, preds)
print("MSE:", mse)