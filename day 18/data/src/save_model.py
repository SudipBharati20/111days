import joblib

def save_model(model, path="model.pkl"):
    joblib.dump(model, path)