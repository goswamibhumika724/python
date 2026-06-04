#Create a bar chart showing the annual Sensex return from 2010 to 2025.
import matplotlib.pyplot as plt 
plt.figure(figsize=(17,7))

bar_color =["#00B7F1","#004BA0"]


years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
sensex_returns = [17.43, -24.64, 25.70, 8.98, 29.89, -5.03, 1.95, 27.91, 5.91, 14.38, 15.75, 21.99, 4.44, 18.74, 13.79, 11.20]

plt.barh(years,sensex_returns,color = bar_color,edgecolor='black',align='center')
plt.xlabel('sensex return(%)')
plt.ylabel('years')
plt.yticks(years)
plt.title('sensex return from 2010 to 2025')
plt.show()