import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import os
# Specify the file path
file_path = 'data/random_data.csv'

# Check if the file exists
try:
    # Load the DataFrame from the file
    df = pd.read_csv(file_path)
except FileNotFoundError:
    # Generate random data if the file is not found
    np.random.seed(42)  # Setting seed for reproducibility
    num_rows = 100
    data = {
        'account_length': np.random.randint(50, 150, num_rows),
        'total_day_charge': np.round(np.random.uniform(20, 60, num_rows), 1),
        'total_eve_charge': np.round(np.random.uniform(5, 25, num_rows), 1),
        'total_night_charge': np.round(np.random.uniform(5, 15, num_rows), 1),
        'total_intl_charge': np.round(np.random.uniform(1, 5, num_rows), 1),
        'customer_service_calls': np.random.randint(0, 5, num_rows),
        'churn': np.random.randint(0, 2, num_rows)
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a file
    df.to_csv(file_path, index=False)

# Plotting the data
x = df['total_day_charge']
y = df['total_eve_charge']

plt.scatter(x, y, c=df['churn'], cmap='viridis', edgecolors='k', alpha=0.8)
plt.xlabel('Total Day Charge')
plt.ylabel('Total Eve Charge')
plt.title('Scatter Plot of Total Day Charge vs Total Eve Charge')
cbar = plt.colorbar()
cbar.set_label('Churn')

plt.show()

# Create DataFrame
df = pd.DataFrame(data)
y = df["churn"].values
X = df[["account_length", "customer_service_calls"]].values

# Create a KNN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=15)
# Fit the classifier to the data
knn.fit(X, y)
X_new = np.array([[33.2, 19.5],
                  [2.3, 24.1],
                  [200.1, 12.3]])
# Predict the labels for the X_new
y_pred = knn.predict(X_new)

# Print the predictions
print("Predictions: {}".format(y_pred))

