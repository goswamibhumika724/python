#Create a step chart showing the prices of gold, silver, and copper over the last 25 years.
import matplotlib.pyplot as plt

years = list(range(2000, 2025))

gold =   [440, 430, 450, 480, 520, 600, 700, 800, 900, 1000,
          1100, 1200, 1400, 1500, 1600, 1800, 1900, 2000, 2100, 2000,
          1900, 1850, 1950, 2050, 2100]

silver = [5, 5.2, 5.5, 6, 6.5, 7, 8, 9, 10, 12,
          14, 16, 18, 20, 22, 24, 25, 26, 28, 27,
          26, 25, 24, 25, 26]

copper = [1.6, 1.5, 1.7, 1.8, 2.0, 2.2, 2.5, 3.0, 3.2, 3.5,
          3.8, 4.0, 4.2, 4.0, 3.8, 4.1, 4.3, 4.5, 4.7, 4.6,
          4.4, 4.3, 4.5, 4.6, 4.8]

plt.figure(figsize=(10,6))
plt.step(years,gold,where='mid',color='red',label='gold')
plt.step(years,silver,where='mid',color='green',label='silver')
plt.step(years,copper,where='mid',color='black',label='copper')
plt.xlabel('years')
plt.xticks(years)
plt.ylabel('price')
plt.title('step plot chart')
plt.legend()
plt.grid(True)
plt.show()