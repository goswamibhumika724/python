#Create a step chart showing the percentage growth of Bitcoin and Ethereum.
import matplotlib.pyplot as plt

years = list(range(2015, 2025))

bitcoin_growth = [0, 30, 120, 400, 200, 300, 500, 800, 1200, 1500]
ethereum_growth = [0, 50, 300, 900, 600, 700, 1200, 2000, 2500, 3000]

plt.figure(figsize=(10,6))
plt.step(years,bitcoin_growth,where='mid',color='orange',label='bitcoin')
plt.step(years,ethereum_growth,where='mid',color='blue',label='ethereum')

plt.xlabel('years')
plt.xticks(years)
plt.ylabel('growth')
plt.title('growth of bitcoin & ethereum')
plt.legend()
plt.grid(True)
plt.show()