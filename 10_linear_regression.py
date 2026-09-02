# linear regression
# ------------------------------------------------------
# There are 2 input features in each exercise.

# Exercise 3: Calculating Monthly Gym RevenueScenario: A gym owner wants to forecast monthly revenue to optimize budget allocation.Input Features ($X$):$X_1$: Total number of active premium members$X_2$: Monthly digital marketing expenditure (in dollars)Target Variable ($Y$): Total monthly revenue (in dollars)Practice Goal: Determine the baseline revenue (intercept) when membership growth and ad spend are zero.
import numpy as np 
from sklearn.linear_model import LinearRegression

# 50 rows for Exercise 3: Calculating Monthly Gym Revenue
# Features: [Active premium members (X1), Marketing spend in $ (X2)]
gym_data = np.array([
    [120, 1500], [180, 2200], [250, 3100], [310, 4000], [400, 5200],
    [140, 1700], [210, 2600], [290, 3700], [350, 4600], [420, 5500],
    [110, 1300], [170, 2100], [230, 2900], [300, 3900], [380, 4900],
    [130, 1600], [190, 2400], [270, 3400], [330, 4300], [410, 5300],
    [105, 1250], [160, 2000], [240, 3000], [320, 4100], [390, 5000],
    [150, 1900], [220, 2800], [280, 3600], [360, 4700], [430, 5600],
    [115, 1400], [175, 2200], [260, 3300], [315, 4050], [395, 5100],
    [135, 1650], [200, 2500], [275, 3500], [340, 4400], [415, 5400],
    [125, 1550], [185, 2300], [245, 3050], [325, 4200], [385, 4950],
    [145, 1800], [215, 2700], [295, 3800], [355, 4650], [425, 5550]
])

# Target Variable: Total monthly revenue in $ (Y)
# Ground Truth Model: Revenue ≈ $5,000 (Base) + ($55 * Members) + ($1.8 * Ad Spend) + Noise
revenue = np.array([
    14320, 18850, 24350, 29280, 36340,
    15760, 21210, 27600, 32540, 37990,
    13390, 18120, 22890, 28510, 34710,
    15040, 19780, 25980, 30890, 37090,
    13030, 17400, 23600, 29990, 35450,
    16670, 22140, 26890, 33260, 38710,
    13840, 18590, 25240, 29620, 35910,
    15400, 20500, 26420, 31620, 37550,
    14660, 19320, 23970, 30440, 35090,
    16220, 21690, 28070, 32890, 38360
])

#create model 
model = LinearRegression()

#model train 
model.fit(gym_data,revenue)

#prediction
#prediction
gym = np.array([[100, 3600]])
print("Predicted revenue for gym with 100 members and $3600 marketing spend is", model.predict(gym))

gym_2 = np.array([[450, 2800]])
print("Predicted revenue for gym_2 with 450 members and $2800 marketing spend is", model.predict(gym_2))

