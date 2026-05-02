from load_data import load_data
from explore import explore_data
from preprocess import preprocess_data
from feature_engineering import create_features
from split_data import split_data
from train_model import train_model
from evaluate_model import evaluate
from save_model import save_model
from predict import load_model, make_prediction

# Load
data = load_data("../data/weather.csv")

# Explore
explore_data(data)

# Preprocess
data = preprocess_data(data)

# Features
X, y = create_features(data)

# Split
X_train, X_test, y_train, y_test = split_data(X, y)

# Train
model = train_model(X_train, y_train)

# Evaluate
evaluate(model, X_test, y_test)

# Save
save_model(model)

# Predict
model = load_model()
sample = [70, 10, 1012]  # humidity, wind, pressure
print("Prediction:", make_prediction(model, sample))