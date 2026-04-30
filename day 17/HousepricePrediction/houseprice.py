import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt 

# 1. Load data
data = pd.read_csv('day 17/HousepricePrediction/house.csv')

# 2. Preprocessing
# Convert Year_Built to Age for better correlation
data['Age'] = 2026 - data['Year_Built']

# 3. Define Features and Target
# We remove 'Price' (target), 'House_ID' (useless), and 'Year_Built' (replaced by Age)
X = data.drop(['Price', 'House_ID', 'Year_Built'], axis=1)
y = data['Price']

# 4. Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred) # Added R-squared to see accuracy percentage

print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared Score: {r2:.2f}') 

# 7. Visualization
plt.figure(figsize=(8, 5))
sns.regplot(x=y_test, y=y_pred, ci=None, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
# Adding a reference line
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.title('Actual vs Predicted Prices (Red line = Trend)')
plt.show()