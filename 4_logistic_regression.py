# logistic regression 
# ----------------------------------------------------------------
# There are 2 input features in each exercise.
#Exercise 3: Real EstateDevelop a logistic regression example that will predict whether a house will Sell within 30 days ($y=1$) or Take longer ($y=0$) based on two input features: Listing price in hundreds of thousands ($x_1$) and Square footage in thousands ($x_2$).

import numpy as np
from sklearn.linear_model import LogisticRegression


# Input features: [Listing price in hundreds of thousands (x1), Square footage in thousands (x2)] (100 rows)
house = np.array([
    [2.5, 1.8], [5.0, 2.2], [3.2, 2.0], [1.8, 1.2], [6.5, 3.5],
    [4.0, 2.5], [7.2, 3.8], [2.2, 1.5], [6.0, 3.0], [3.5, 2.1],
    [1.5, 1.0], [5.5, 2.8], [3.0, 1.9], [4.5, 2.6], [8.0, 4.2],
    [2.0, 1.4], [5.2, 2.5], [3.8, 2.2], [2.8, 1.7], [6.2, 3.2],
    [1.9, 1.3], [4.2, 2.4], [7.5, 4.0], [3.3, 2.0], [4.8, 2.7],
    [2.6, 1.8], [5.8, 2.9], [3.1, 1.9], [4.6, 2.6], [6.8, 3.4],
    [2.1, 1.4], [4.9, 2.5], [7.0, 3.6], [3.4, 2.1], [5.1, 2.7],
    [2.4, 1.6], [5.6, 3.0], [3.2, 2.0], [3.9, 2.3], [5.3, 2.8],
    [1.7, 1.2], [4.7, 2.6], [7.8, 4.1], [3.6, 2.2], [4.4, 2.5],
    [2.7, 1.8], [5.4, 2.8], [3.5, 2.1], [4.3, 2.4], [6.4, 3.2],
    [2.3, 1.6], [3.8, 2.3], [6.1, 3.1], [1.8, 1.1], [8.2, 4.3],
    [4.5, 2.6], [6.7, 3.5], [3.0, 1.9], [5.0, 2.5], [2.5, 1.7],
    [1.6, 1.1], [6.3, 3.3], [3.2, 2.0], [4.1, 2.4], [7.4, 3.9],
    [2.2, 1.5], [5.1, 2.6], [3.9, 2.3], [2.9, 1.8], [5.7, 2.9],
    [2.0, 1.3], [4.8, 2.5], [7.1, 3.7], [3.3, 2.0], [4.6, 2.5],
    [1.5, 1.0], [4.0, 2.2], [7.6, 4.0], [3.1, 1.9], [4.4, 2.4],
    [2.8, 1.9], [5.3, 2.7], [3.7, 2.2], [4.2, 2.3], [6.2, 3.1],
    [2.5, 1.7], [4.3, 2.4], [5.9, 3.0], [3.0, 1.8], [5.5, 2.8],
    [2.1, 1.4], [4.9, 2.6], [6.9, 3.6], [3.5, 2.1], [4.7, 2.5],
    [2.4, 1.6], [5.0, 2.5], [3.6, 2.1], [4.1, 2.3], [6.0, 3.0]
])

# Output labels: Sell within 30 days (1) or Take longer (0) (100 rows)
result = np.array([
    1, 0, 1, 1, 0,
    1, 0, 1, 0, 1,
    1, 0, 1, 1, 0,
    1, 0, 1, 1, 0,
    1, 1, 0, 1, 1,
    1, 0, 1, 1, 0,
    1, 1, 0, 1, 0,
    1, 0, 1, 1, 0,
    1, 1, 0, 1, 1,
    1, 0, 1, 1, 0,
    1, 1, 0, 1, 0,
    1, 0, 1, 1, 1,
    1, 0, 1, 1, 0,
    1, 1, 1, 1, 0,
    1, 1, 0, 1, 1,
    1, 1, 0, 1, 1,
    1, 0, 1, 1, 0,
    1, 1, 0, 1, 0,
    1, 1, 0, 1, 1,
    1, 1, 1, 1, 0
])

#create model
model = LogisticRegression()
print("model training started.....")

#model train
model.fit(house,result) # input, label (output)

print("model training complete.....")

# Prediction for a new house [Listing price in hundreds of thousands, Square footage in thousands]
house_1 = np.array([[3.5, 2.7]])
prediction = model.predict(house_1)

print("House_1 prediction (0: Take longer, 1: Sell within 30 days) = ", prediction)
print("Sell within 30 days probability = ", model.predict_proba(house_1))

house_2 = np.array([[7.5, 2.3]])
prediction = model.predict(house_2)

print("House_1 prediction (0: Take longer, 1: Sell within 30 days) = ", prediction)
print("Sell within 30 days probability = ", model.predict_proba(house_2))

# Model accuracy
print("Model accuracy = ", model.score(house, result))