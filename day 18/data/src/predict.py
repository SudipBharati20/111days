import joblib

def load_model(path="model.pkl"):
    return joblib.load(path)

def make_prediction(model, sample):
    prediction = model.predict([sample])
    return prediction