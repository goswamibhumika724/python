# linear regression
# ------------------------------------------------------
# There are 2 input features in each exercise.

# Exercise 5: Software Developer Salary PredictionScenario: A tech recruitment platform wants to build a pricing model to estimate fair market salaries for software engineers.Input Features ($X$):$X_1$: Years of professional coding experience$X_2$: Number of specialized technical certifications earnedTarget Variable ($Y$): Annual salary (in thousands of dollars)Practice Goal: Evaluate how much value a certification adds to a developer's salary compared to an extra year of experience.
import numpy as np 
from sklearn.linear_model import LinearRegression

# 50 rows for Exercise 5: Software Developer Salary Prediction
# Features: [Years of coding experience (X1), Technical certifications (X2)]
dev_data = np.array([
    [1.5, 1], [4.0, 2], [7.5, 3], [10.0, 4], [2.0, 0],
    [5.5, 2], [8.0, 4], [3.0, 1], [6.5, 3], [12.0, 5],
    [1.0, 0], [4.5, 3], [9.0, 4], [2.5, 1], [6.0, 2],
    [8.5, 3], [11.0, 5], [3.5, 2], [7.0, 3], [1.8, 1],
    [5.0, 2], [10.5, 4], [2.2, 0], [6.8, 3], [8.8, 4],
    [3.2, 1], [7.2, 2], [11.5, 5], [1.2, 0], [4.8, 3],
    [9.5, 4], [2.8, 1], [6.2, 2], [8.2, 3], [12.5, 5],
    [3.8, 2], [7.8, 4], [1.6, 1], [5.2, 2], [10.2, 4],
    [2.4, 0], [6.6, 3], [8.6, 4], [3.4, 1], [7.4, 3],
    [11.8, 5], [1.4, 0], [4.2, 2], [9.2, 4], [2.6, 1]
])

# Target: Annual salary in thousands of dollars (Y)
salary = np.array([
     68.5,  92.0, 126.5, 155.0,  67.0,
    104.5, 137.0,  81.5, 118.0, 175.5,
     58.0,  99.5, 146.0,  77.0, 109.0,
    134.5, 168.0,  88.5, 122.0,  71.0,
    101.0, 160.5,  69.5, 120.0, 144.0,
     83.0, 119.5, 172.0,  60.5, 102.0,
    151.0,  79.5, 110.5, 131.0, 181.0,
     91.0, 135.0,  69.0, 102.5, 157.0,
     71.5, 118.5, 142.0,  85.0, 125.5,
    174.0,  62.0,  93.5, 147.5,  78.0
])

# Create model 
model = LinearRegression()

# Model train 
model.fit(dev_data, salary)

# Prediction 1: Developer with 5 years experience and 3 certifications
dev_1 = np.array([[9.0, 6]])
print("Predicted salary for developer with 9 yrs exp and 6 certs is $", model.predict(dev_1))

# Prediction 2: Developer with 8 years experience and 1 certification
dev_2 = np.array([[1.0, 9]])
print("Predicted salary for developer with 1 yrs exp and 9 cert is $", model.predict(dev_2))