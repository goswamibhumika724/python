# linear regression
# ------------------------------------------------------
# There are 2 input features in each exercise.

# Exercise 2: Estimating Car Fuel EfficiencyScenario: An automotive blog wants to predict a vehicle's fuel economy to help consumers evaluate fuel costs.Input Features ($X$):$X_1$: Engine displacement size (in liters)$X_2$: Total vehicle weight (in pounds or kilograms)Target Variable ($Y$): Fuel efficiency (Miles Per Gallon - MPG)Practice Goal: Observe how both engine size and weight negatively correlate with fuel efficiency (negative coefficients).
import numpy as np 
from sklearn.linear_model import LinearRegression

car_specs = np.array([
    [1.5, 2350], [2.0, 2800], [2.5, 3250], [3.5, 3900], [5.0, 4600],
    [1.6, 2450], [2.2, 2950], [3.0, 3500], [4.0, 4150], [5.3, 4750],
    [1.4, 2200], [1.8, 2600], [2.4, 3100], [3.3, 3750], [4.6, 4400],
    [1.5, 2400], [2.0, 2750], [2.8, 3400], [3.6, 3950], [5.7, 4900],
    [1.3, 2150], [1.9, 2700], [2.5, 3300], [3.8, 4050], [4.8, 4550],
    [1.6, 2500], [2.1, 2900], [3.2, 3650], [4.2, 4250], [5.2, 4700],
    [1.4, 2250], [2.0, 2850], [2.7, 3350], [3.5, 3850], [4.5, 4350],
    [1.7, 2550], [2.3, 3050], [3.0, 3600], [4.0, 4100], [6.0, 5100],
    [1.5, 2300], [1.8, 2650], [2.6, 3200], [3.4, 3800], [4.4, 4300],
    [1.6, 2480], [2.2, 3000], [3.1, 3550], [3.9, 4000], [5.0, 4650]
])

# Target: Fuel efficiency in MPG (Y)
mpg = np.array([
    36.5, 30.2, 26.0, 19.8, 14.2,
    35.1, 28.5, 23.4, 17.9, 13.5,
    38.2, 32.4, 27.1, 21.0, 15.6,
    36.0, 31.0, 24.5, 19.2, 12.0,
    39.5, 31.8, 25.4, 18.5, 14.8,
    34.8, 29.5, 22.8, 17.2, 13.8,
    37.6, 29.8, 25.0, 20.3, 16.1,
    33.9, 27.9, 23.0, 18.2, 11.2,
    36.8, 32.0, 26.5, 20.7, 16.5,
    35.0, 28.2, 23.1, 18.8, 14.0
])

#create model 
model = LinearRegression()

#model train 
model.fit(car_specs,mpg)

#prediction
car = np.array([[3.10,4001]])
print("Predicted MPG for car with 3.10L engine and 4001 lbs weight is",model.predict(car))

car_2 = np.array([[2.14,2141]])
print("Predicted MPG for car_2 with 2.14L engine and 2141 lbs weight is",model.predict(car_2))

