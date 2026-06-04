#Create a contourf chart showing sugar quantity (grams), tea boiling time (minutes), and user ratings.
import numpy as np
import matplotlib.pyplot as plt

sugar = np.linspace(0, 20, 100)
boiling_time = np.linspace(2, 12, 100)
Sugar, Time = np.meshgrid(sugar, boiling_time)

Ratings = 10 - 0.04 * (Sugar - 10)**2 - 0.15 * (Time - 5)**2
Ratings = np.clip(Ratings, 1, 10)

contour = plt.contourf(Sugar, Time, Ratings, levels=15, cmap='viridis')
lines = plt.contour(Sugar, Time, Ratings, levels=7, colors='white', alpha=0.3)
plt.clabel(lines, inline=True, fontsize=10, fmt='%.1f')

cbar = plt.colorbar(contour)
cbar.set_label('User Ratings (1-10)', fontsize=12, labelpad=10)

plt.title('Impact of Sugar Quantity & Boiling Time on Tea Ratings', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Sugar Quantity (grams)', fontsize=12)
plt.ylabel('Tea Boiling Time (minutes)', fontsize=12)

plt.plot(10, 5, marker='*', color='gold', markersize=15, label='Optimal Recipe')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.2, linestyle='--')
plt.show()