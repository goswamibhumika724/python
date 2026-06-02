#Create a line chart to display the number of ODI matches played each year in men's cricket from 2000 to 2025.
import matplotlib.pyplot as plt
import numpy as np

years = list(range(2000,2026))
matches =[141, 119, 147, 153, 126, 122, 164, 177, 124, 152, 141, 147, 104, 144, 123, 141, 98, 129, 128, 151, 44, 71, 131, 167, 115, 95]


plt.title('ODI matches 2000 to 2025')
plt.xlabel('years',fontsize='11',fontweight='bold',labelpad=10)
plt.ylabel('matches',fontsize='11',fontweight='bold',labelpad=10)

plt.grid(which='both',linestyle='dotted',linewidth=0.7)
plt.plot(years, matches, label='ODI Matches (India)')
plt.legend(loc='upper left')
plt.xlim(left=1999,right=2026)
plt.ylim(bottom=44,top=180)

plt.yticks(np.arange(0,max(matches)+26,26))
plt.xticks(years,rotation=45)
plt.tight_layout()
plt.show()