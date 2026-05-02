from sklearn.metrics import mean_absolute_error

def evaluate(model, X_test, y_test):
    preds = model.predict(X_test)
    error = mean_absolute_error(y_test, preds)
    print("MAE:", error)