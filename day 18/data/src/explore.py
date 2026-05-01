def explore_data(data):
    print("First 5 rows:\n", data.head())
    print("\nInfo:\n")
    print(data.info())
    print("\nSummary:\n", data.describe())