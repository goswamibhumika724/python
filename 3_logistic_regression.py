# logistic regression 
# ----------------------------------------------------------------
# There are 2 input features in each exercise.

#Exercise 2: E-CommerceDevelop a logistic regression example that will predict whether an online shopper will Complete a Purchase ($y=1$) or Abandon the Cart ($y=0$) based on two input features: Time spent on site in minutes ($x_1$) and Number of pages viewed ($x_2$).
import numpy as np
from sklearn.linear_model import LogisticRegression

# Input features: [Time spent on site in minutes (x1), Number of pages viewed (x2)] (100 rows)
numbers = np.array([
    [2.5, 2], [12.0, 8], [5.5, 4], [1.0, 1], [15.5, 12],
    [8.0, 6], [18.0, 14], [3.0, 2], [14.0, 10], [4.5, 3],
    [1.5, 1], [16.0, 11], [6.0, 5], [10.5, 7], [20.0, 16],
    [2.0, 2], [11.5, 8], [7.0, 5], [4.0, 3], [13.5, 9],
    [1.2, 1], [9.0, 6], [17.5, 13], [5.0, 4], [8.5, 6],
    [3.5, 3], [12.5, 9], [6.5, 5], [9.5, 7], [14.5, 10],
    [1.8, 1], [10.0, 7], [16.5, 12], [4.8, 3], [11.0, 8],
    [3.2, 2], [13.0, 9], [5.8, 4], [7.5, 5], [12.2, 8],
    [1.1, 1], [10.2, 7], [18.5, 15], [6.2, 4], [9.2, 6],
    [2.8, 2], [11.8, 8], [6.8, 5], [8.8, 6], [13.8, 9],
    [2.2, 2], [7.2, 5], [13.2, 9], [1.9, 1], [19.0, 15],
    [9.8, 7], [15.0, 11], [6.4, 4], [10.8, 7], [3.8, 2],
    [1.3, 1], [14.2, 10], [5.2, 3], [9.4, 6], [17.0, 13],
    [2.4, 2], [11.2, 8], [7.8, 5], [4.2, 3], [12.8, 9],
    [1.6, 1], [10.4, 7], [15.8, 11], [5.6, 4], [8.2, 6],
    [1.0, 1], [8.6, 6], [18.0, 14], [6.0, 4], [9.6, 7],
    [3.0, 2], [12.0, 8], [7.0, 5], [8.0, 6], [14.0, 10],
    [2.5, 2], [9.0, 6], [13.0, 9], [5.0, 3], [12.5, 8],
    [1.4, 1], [10.5, 7], [16.0, 12], [7.5, 5], [9.5, 6],
    [2.0, 2], [11.0, 8], [6.5, 4], [8.5, 6], [13.5, 9]
])

# Output labels: Complete a Purchase (1) or Abandon the Cart (0) (100 rows)
result = np.array([
    0, 1, 0, 0, 1,
    0, 1, 0, 1, 0,
    0, 1, 0, 1, 1,
    0, 1, 0, 0, 1,
    0, 1, 1, 0, 0,
    0, 1, 0, 1, 1,
    0, 1, 1, 0, 1,
    0, 1, 0, 0, 1,
    0, 1, 1, 0, 0,
    0, 1, 0, 0, 1,
    0, 0, 1, 0, 1,
    1, 1, 0, 1, 0,
    0, 1, 0, 0, 1,
    0, 1, 0, 0, 1,
    0, 1, 1, 0, 0,
    0, 0, 1, 0, 0,
    0, 1, 0, 0, 1,
    0, 0, 1, 0, 1,
    0, 1, 1, 0, 0,
    0, 1, 0, 0, 1
])

#create model
model = LogisticRegression()
print("model training started.....")

#model train
model.fit(numbers,result) # input, label (output)

print("model training complete.....")

# Prediction for a new online shopper [Time spent in minutes, Number of pages viewed]
shopper_1 = np.array([[14.5, 18]])
prediction = model.predict(shopper_1)

print("Shopper_1 purchase prediction (0: Abandon Cart, 1: Complete Purchase) = ", prediction)
print("purchase probability = ", model.predict_proba(shopper_1))

shopper_2 = np.array([[1.0, 12]])
prediction = model.predict(shopper_2)

print("Shopper_2 purchase prediction (0: Abandon Cart, 1: Complete Purchase) = ", prediction)
print("purchase probability = ", model.predict_proba(shopper_2))

# Model accuracy
print("Model accuracy = ", model.score(numbers, result))