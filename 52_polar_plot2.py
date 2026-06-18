# Polar Chart

# Create a polar chart showing the number of runs scored by Virat Kohli in different field directions.
import numpy as np
import matplotlib.pyplot as plt

directions = ['Fine Leg', 'Square Leg', 'Midwicket', 'Mid-on',
              'Mid-off', 'Cover', 'Point', 'Third Man']

degrees = [20, 60, 110, 150, 210, 250, 290, 330]
runs = [6, 23, 65, 51, 28, 45, 38, 17]

theta = np.radians(degrees)

ax = plt.subplot(projection='polar')

ax.bar(theta, runs, width=np.radians(30), alpha=0.8)

ax.set_xticks(theta)
ax.set_xticklabels(directions)

ax.set_title("Virat Kohli Runs by Field Direction")

plt.show()