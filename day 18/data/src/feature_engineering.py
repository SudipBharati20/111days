def create_features(data):
    X = data.drop("temperature", axis=1)
    y = data["temperature"]
    return X, y