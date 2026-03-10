from sklearn.linear_model import LogisticRegression
import numpy as np

# Training data
# Study hours
X = np.array([[1], [2], [3], [4], [5], [6]])

# 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 1, 1, 1])

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# User input
hours = int(input("Enter study hours: "))

prediction = model.predict([[hours]])

if prediction[0] == 1:
    print("Prediction: Student will PASS")
else:
    print("Prediction: Student will FAIL")
