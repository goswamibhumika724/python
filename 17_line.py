#Create a line chart to display the number of T20 matches played each year in men's cricket from 2000 to 2025.
import matplotlib.pyplot as plt 
years = list(range(2000,2026))
matches=[0, 0, 0, 0, 0, 1, 2, 25, 18, 47, 51, 40, 83, 64, 89, 62, 101, 65, 92, 312, 157, 341, 493, 384, 466, 395]

plt.plot(years,matches,color='blue')
plt.title('T20 matches played in india (2000-2025)')
plt.xlabel('years')
plt.xticks(years,rotation=45)
plt.ylabel('matches')
plt.grid(True)
plt.show()
