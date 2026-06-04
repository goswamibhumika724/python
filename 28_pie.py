#Create a pie chart showing the percentage of students in Gujarat who opted for Commerce, Arts, Science, and Diploma after the 10th standard.
import matplotlib.pyplot as plt 


labels = ['Commerce', 'Arts', 'Science', 'Diploma']
sizes = [38, 22, 30, 10]
bar_colors = [   
    "#004BA0", 
    "#FFFF00",
    "#00B7F1",
    "#EA1B85"
]

plt.pie(sizes,labels=labels,colors=bar_colors,autopct='%.1f%%')
plt.title('pie chart')
plt.show()