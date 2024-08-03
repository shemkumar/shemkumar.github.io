import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Filter out only 'setosa' and 'versicolor' classes
mask = y < 2
X, y = X[mask], y[mask]

# Find out how many cases are there. Length of X
num_cases = len(X)
print(f"Number of cases: {num_cases}")

# Print first 10 cases of X and y
print("First 10 cases of X:\n", X[:10])
print("First 10 cases of y:\n", y[:10])

# Find what attributes are there for X
attributes = iris.feature_names
print("Attributes of X:\n", attributes)

# Find mean and std of each attribute
means = np.mean(X, axis=0)
stds = np.std(X, axis=0)

print("Means of each attribute:\n", means)
print("Standard deviations of each attribute:\n", stds)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the SVC with linear kernel
svc = SVC(kernel='linear')
svc.fit(X_train, y_train)

# Create sample test data
sample_data = np.array([[5.0, 3.5, 1.3, 0.3], [6.0, 2.9, 4.5, 1.5]])
sample_data = scaler.transform(sample_data)

# Predict the class
predictions = svc.predict(sample_data)
print("Predictions for the sample data:", predictions)

# Predict on the test set
y_pred = svc.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy with linear kernel: {accuracy:.2f}")

# If accuracy is below 95%, try different kernels
if accuracy < 0.95:
    svc_rbf = SVC(kernel='rbf')
    svc_rbf.fit(X_train, y_train)
    y_pred_rbf = svc_rbf.predict(X_test)
    accuracy_rbf = accuracy_score(y_test, y_pred_rbf)
    print(f"Accuracy with RBF kernel: {accuracy_rbf:.2f}")
    
    svc_poly = SVC(kernel='poly')
    svc_poly.fit(X_train, y_train)
    y_pred_poly = svc_poly.predict(X_test)
    accuracy_poly = accuracy_score(y_test, y_pred_poly)
    print(f"Accuracy with Polynomial kernel: {accuracy_poly:.2f}")
