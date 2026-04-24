def train():
    data = load_data()
    X, y = preprocess(data)

    model = LinearRegression()
    model.fit(X, y)

    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train()