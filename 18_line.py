#Create a line chart to display the number of ODI, Test, and T20 matches played each year in men's cricket from 2000 to 2025.
import matplotlib.pyplot as plt


years = list(range(2000, 2026))

# Total number of Test matches played per year
test = [
    45, 49, 54, 49, 52, 47, 46, 36, 47, 41, 
    43, 39, 43, 42, 41, 43, 47, 47, 43, 39, 
    22, 44, 43, 41, 45, 44
]

# Total number of ODI matches played per year
odi = [
    134, 117, 149, 119, 131, 110, 155, 142, 113, 146, 
    141, 147, 126, 128, 131, 143, 112, 129, 124, 150, 
    42, 80, 161, 185, 118, 125
]

# Total number of T20I matches played per year (Format introduced in 2005)
t20= [
    0, 0, 0, 0, 0, 3, 18, 26, 23, 44, 
    23, 27, 72, 57, 46, 56, 82, 70, 84, 194, 
    78, 234, 290, 252, 351, 310
]

plt.plot(years,test,color='red',linewidth=2,label='Test')
plt.plot(years,odi,color='blue',linewidth=2,label='ODI')
plt.plot(years,t20,color='green',linewidth=2,label='T20')
plt.title('Test,ODI,T20 matches played in india (2000-2025)')
plt.xlabel('years')
plt.xticks(years,rotation=45)
plt.ylabel('numbers of matches')
plt.grid(True)
plt.legend()
plt.ylim(0,360)
plt.show()
