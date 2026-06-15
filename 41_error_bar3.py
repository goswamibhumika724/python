# Error Bar Chart

# Create an error bar chart showing the sales performance of 5 products over 30 days.

import matplotlib.pyplot as plt

# 1. Product names list
products = [
    'TechGadget X', 'Smart Gizmo', 'Eco Widget', 'Alpha Device', 'Omega Appliance'
]

# Average daily sales over 30 days
average = [245.8, 192.4, 155.1, 122.6, 98.3]

# Sales performance variance / daily error margins (Standard Deviation)
errors = [32.5, 18.2, 22.4, 11.8, 26.7]

plt.errorbar(products,average,errors,color='blue',capsize=10,fmt='o')
plt.title("sales with error bar chart")
plt.xlabel("products")
plt.ylabel("average")
plt.grid()
plt.tight_layout()
plt.show()