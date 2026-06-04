#Create a pie chart showing the smartphone market share of Realme, Redmi, Oppo, Vivo, Samsung, Apple, Nokia, and others.
import matplotlib.pyplot as plt 

brands = ['Realme', 'Redmi', 'Oppo', 'Vivo', 'Samsung', 'Apple', 'Nokia', 'Others']
market_share = [12, 18, 15, 14, 20, 10, 5, 6]
bar_colors = [   
    "#004BA0", # Mumbai Indians (Blue)
    "#FFFF00", # Chennai Super Kings (Yellow)
    "#3A225D", # Kolkata Knight Riders (Purple)
    "#EA1B85", # Rajasthan Royals (Pink)
    "#FF822A", # Sunrisers Hyderabad (Orange)
    "#1B2133", # Gujarat Titans (Navy Blue)
    "#EC1C24", # Royal Challengers Bengaluru (Red)
    "#00B7F1"  # Deccan Chargers (Sky Blue)
    ]

plt.pie(market_share,labels=brands,colors=bar_colors,autopct='%.1f%%')
plt.title('pie chart')
plt.show()