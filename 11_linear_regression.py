# linear regression
# ------------------------------------------------------
# There are 2 input features in each exercise.

# Exercise 4: Estimating Daily Ice Cream SalesScenario: An ice cream parlor owner wants to forecast daily product demand to prevent shortages or food waste.Input Features ($X$):$X_1$: Maximum daily temperature (in Fahrenheit or Celsius)$X_2$: Estimated daily foot traffic count passing the shopTarget Variable ($Y$): Number of ice cream cones sold per dayPractice Goal: Make a prediction for an upcoming hot weekend day with high projected foot traffic.
import numpy as np 
from sklearn.linear_model import LinearRegression

# 50 rows for Exercise 4: Estimating Daily Ice Cream Sales
# Features: [Max Daily Temperature in °C (X1), Foot Traffic Count (X2)]
icecream_data = np.array([
    [22.5, 450], [31.0, 920], [18.2, 310], [28.4, 780], [35.2, 1150],
    [20.1, 410], [33.5, 1020], [16.5, 260], [29.8, 850], [24.0, 560],
    [15.0, 220], [32.1, 960], [25.5, 640], [27.9, 730], [36.5, 1220],
    [19.4, 380], [30.5, 890], [26.2, 690], [23.1, 510], [34.0, 1080],
    [17.8, 290], [28.0, 750], [34.8, 1110], [21.5, 470], [31.8, 940],
    [19.0, 360], [33.0, 1040], [24.8, 610], [27.1, 710], [35.8, 1180],
    [16.0, 250], [29.2, 820], [36.0, 1200], [25.0, 620], [32.5, 990],
    [21.0, 440], [33.8, 1060], [22.0, 480], [26.8, 670], [34.5, 1100],
    [17.2, 280], [28.7, 800], [37.0, 1250], [23.5, 530], [30.1, 880],
    [20.5, 430], [31.5, 930], [25.8, 660], [27.5, 720], [35.0, 1140]
])

# Target: Number of ice cream cones sold per day (Y)
cones_sold = np.array([
    135, 312,  94, 255, 395,
    118, 350,  78, 285, 168,
     65, 328, 195, 238, 415,
    108, 302, 215, 152, 365,
     88, 248, 382, 138, 320,
    102, 358, 178, 228, 405,
     72, 275, 410, 185, 335,
    125, 362, 142, 220, 372,
     82, 268, 428, 158, 298,
    120, 315, 205, 232, 388
])

# Create model 
model = LinearRegression()

# Model train 
model.fit(icecream_data, cones_sold)

# Practice Goal: Prediction for an upcoming hot weekend day (36.5°C, 1200 foot traffic)
hot_weekend_day = np.array([[40.5, 1200]])
print("Predicted cones sold on a hot weekend day with 40.5°C temp and 1200 foot traffic is", model.predict(hot_weekend_day))

# Normal day prediction (22.0°C, 500 foot traffic)
normal_day = np.array([[18.0, 300]])
print("Predicted cones sold on a normal day with 18.0°C temp and 300 foot traffic is", model.predict(normal_day))
