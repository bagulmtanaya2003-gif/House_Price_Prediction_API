# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("housing_price_dataset.csv")

print(df.head())
df.info()
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.shape)
print(df.columns)

# Save cleaned dataset
df.to_csv("clean_housing.csv", index=False)

# Plot price distribution
plt.figure(figsize=(8,5))
plt.hist(df["Price"], bins=20, color="skyblue", edgecolor="black", linewidth=1.2)
plt.title("Price Distribution", fontsize=14, fontweight="bold")
plt.xlabel("Price", fontsize=12)
plt.ylabel("Number of Houses", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()

# Square Feet vs Price
plt.figure(figsize=(8,5))
plt.scatter(df["SquareFeet"], df["Price"], color="green", edgecolors="black", s=50)
plt.title("Square Feet vs Price", fontsize=14, fontweight="bold")
plt.xlabel("Square Feet", fontsize=12)
plt.ylabel("Price", fontsize=12)
plt.grid(linestyle="--", alpha=0.6)
plt.show()

# Create correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="YlGnBu", linewidths=1)
plt.title("Correlation Heatmap", fontsize=14, fontweight="bold")
plt.show()

# Create box plot
plt.figure(figsize=(6,5))
plt.boxplot(df["Price"], patch_artist=True,
            boxprops=dict(facecolor="skyblue", color="black"),
            medianprops=dict(color="red", linewidth=2),
            whiskerprops=dict(color="black"),
            capprops=dict(color="black"),
            flierprops=dict(marker="o", markerfacecolor="red", markersize=6))
plt.title("Price Box Plot", fontsize=14, fontweight="bold")
plt.ylabel("Price", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Create label encoder
encoder = LabelEncoder()
df["Neighborhood"] = encoder.fit_transform(df["Neighborhood"])
print(df.head())

# Select input features
X = df[["SquareFeet", "Bedrooms", "Bathrooms", "Neighborhood", "YearBuilt"]]
y = df["Price"]

# Show feature shape
print(X.shape)
# Show target shape
print(y.shape)

print(X.head())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
# Train model
model.fit(X_train, y_train)

# Predict price
y_pred = model.predict(X_test)

# Compare actual and predicted values
result = pd.DataFrame({
    "Actual Price": y_test,
    "Predicted Price": y_pred
})
print(result.head())

# Import evaluation metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Calculate MAE
mae = mean_absolute_error(y_test, y_pred)
print("MAE :", mae)

# Calculate MSE
mse = mean_squared_error(y_test, y_pred)
print("MSE :", mse)

# Calculate RMSE
rmse = np.sqrt(mse)
print("RMSE :", rmse)

# Calculate R2 Score
r2 = r2_score(y_test, y_pred)
print("R2 Score :", r2)

import joblib

# Save trained model
joblib.dump(model, "house_price_model.pkl")

# Save label encoder
joblib.dump(encoder, "encoder.pkl")
print("Model and Encoder Saved Successfully")