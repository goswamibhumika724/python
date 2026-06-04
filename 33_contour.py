#Create a contour chart showing longitude, latitude, and internet signal strength.
import numpy as np
import matplotlib.pyplot as plt

longitude = np.linspace(70, 75, 50)
latitude = np.linspace(20, 25, 50)

longitude, latitude = np.meshgrid(longitude, latitude)

signal = np.sin(longitude) + np.cos(latitude)

cs = plt.contour(
    longitude,
    latitude,
    signal,
    levels=10,
    colors='black',
    linestyles='dashed'
)

plt.clabel(cs)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Contour Chart - Signal Strength")

plt.show()