import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import os
# Function to generate random data
def generate_random_data(num_rows=5):
    np.random.seed(42)  # Setting seed for reproducibility
    data = {
        'account_length': np.random.randint(50, 150, num_rows),
        'total_day_charge': np.round(np.random.uniform(20, 90, num_rows), 1),
        'total_eve_charge': np.round(np.random.uniform(5, 60, num_rows), 1),
        'total_night_charge': np.round(np.random.uniform(5, 15, num_rows), 1),
        'total_intl_charge': np.round(np.random.uniform(1, 5, num_rows), 1),
        'customer_service_calls': np.random.randint(0, 5, num_rows),
        'churn': np.zeros(num_rows)  # Initialize churn column with zeros
    }
    condition1 = (data['total_day_charge'] > 75) & (data['total_eve_charge'] > 55)
    condition2 = (data['total_day_charge'] < 75) & (data['total_eve_charge'] > 55)
    data['churn'][condition1] = np.random.choice([1, 0], size=np.sum(condition1), p=[0.75, 0.25])
    data['churn'][condition2] = np.random.choice([1,0], size=np.sum(condition2), p=[0.9, 0.1])
    return pd.DataFrame(data)

# Specify the file path
file_path = 'data/random_data.csv'

# Check if the file exists
if os.path.isfile(file_path):
    # Load the DataFrame from the file
    df = pd.read_csv(file_path)
else:
    # Generate random data and save it to a file
    df = generate_random_data(250)
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
y = df["churn"].values
X = df[["account_length", "customer_service_calls"]].values

# Create a KNN classifier with 15 neighbors
knn = KNeighborsClassifier(n_neighbors=15)
# Fit the classifier to the data
knn.fit(X, y)
X_new = np.array([[33.22, 192.5],
                  [2.3, 234.1],
                  [2022.2, 12.3]])
# Predict the labels for the X_new
y_pred = knn.predict(X_new)

# Print the predictions
print("Predictions: {}".format(y_pred))
plt.show()


