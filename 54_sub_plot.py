#  Dashboard (Multiple Charts)

# Create a dashboard containing 4 different chart types on a single screen. All charts should represent different aspects of the same topic. For example:

#  Line Chart: Monthly sales trend
#  Bar Chart: Product-wise sales
#  Pie Chart: Market share by product
#  Scatter Chart: Sales vs Profit analysis

import matplotlib.pyplot as plt
import numpy as np

# ---------------- DATA ----------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

monthly_sales = [120000, 135000, 128000, 150000, 170000, 165000,
                 180000, 190000, 175000, 200000, 210000, 230000]

products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
product_sales = [320000, 280000, 250000, 190000, 160000]

market_share = [28, 24, 20, 16, 12]

profit = [15000, 18000, 16000, 22000, 26000, 24000,
          30000, 32000, 28000, 35000, 38000, 45000]



# ---------------- LINE CHART ----------------
plt.subplot(2, 2, 1)
plt.plot(months, monthly_sales, marker='o', color='blue', linewidth=2)
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)

# ---------------- BAR CHART ----------------
plt.subplot(2, 2, 2)
bars = plt.bar(products, product_sales, color='skyblue', edgecolor='black')

for bar in bars:
    bar.set_hatch('//')

plt.title("Product-wise Sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.grid(True, linestyle='--', alpha=0.6)

# ---------------- PIE CHART ----------------
plt.subplot(2, 2, 3)
colors = ["#4CAF50", "#2196F3", "#FF9800", "#9C27B0", "#F44336"]

plt.pie(market_share,
        labels=products,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors)

plt.title("Market Share by Product")


# ---------------- SCATTER CHART ----------------
plt.subplot(2, 2, 4)
plt.scatter(monthly_sales, profit,
            color='red',
            s=70,
            alpha=0.7,
            edgecolors='black')

plt.title("Sales vs Profit Analysis")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True, linestyle='--', alpha=0.6)

# ---------------- FINAL LAYOUT ----------------
plt.tight_layout()
plt.show()