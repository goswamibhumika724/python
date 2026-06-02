#Create a line chart to display the number of Test matches played each year in men's cricket from 2000 to 2025. 
import matplotlib.pyplot as plt
import numpy as np
years = list(range(2000,2026))
matches = [
    43, 53, 54, 48, 51, 49, 46, 36, 46, 41, 
    43, 39, 42, 42, 41, 43, 47, 47, 48, 39, 
    22, 44, 43, 33, 42, 38
]


plt.title('test matches 2000 to 2025')
plt.xlabel('years',fontsize='11',fontweight='bold',labelpad=10)
plt.ylabel('matches',fontsize='11',fontweight='bold',labelpad=10)

plt.grid(which='both',linestyle='dotted',linewidth=0.7)
plt.plot(years, matches, label='Test Matches (India)')
plt.legend(loc='upper left')

plt.xlim(left=1999,right=2026)
plt.ylim(bottom=10,top=65)

plt.yticks(np.arange(10,65,10))
plt.xticks(years,rotation=45)
plt.tight_layout()
plt.show()