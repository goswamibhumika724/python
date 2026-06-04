#Create a step chart showing changes in Nifty and Sensex over time.
import matplotlib.pyplot as plt

years = list(range(2010, 2025))

nifty = [5000, 5200, 5400, 6000, 6500, 7000, 8000, 9000, 10000,
         11000, 12000, 13000, 15000, 17000, 19000]

sensex = [17000, 17500, 18000, 20000, 21000, 22000, 25000, 27000, 29000,
          31000, 33000, 35000, 40000, 60000, 70000]

plt.figure(figsize=(10,6))
plt.step(years,nifty,where='mid',color='grey',label='nifty')
plt.step(years,sensex,where='mid',color='purple',label='sensex')

plt.xlabel('years')
plt.xticks(years)
plt.ylabel('index value')
plt.title('nifty and sensex over time')
plt.legend()
plt.grid(True)
plt.show()