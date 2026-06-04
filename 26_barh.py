#Create a bar chart showing the yearly gold price increase Rate from 2010 to 2025.
import matplotlib.pyplot as plt 
plt.figure(figsize=(10,6))
bar_color =["#EC1C24","#3A225D"]

# Yearly data from 2010 to 2025
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
rates = [29.5, 10.2, 7.0, -28.3, -1.5, -10.4, 8.5, 13.1, -1.6, 18.3, 25.1, -3.6, -0.2, 13.1, 13.5, 12.3]

plt.barh(years,rates,color = bar_color,edgecolor='black',align='center')
plt.xlabel('gold rate change (%)')
plt.xticks(range(-30, 35, 5))
plt.ylabel('years')
plt.yticks(years)
plt.title('gold rates change by year')
plt.show()