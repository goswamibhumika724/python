#create KDE chart of buying car 1st time 
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
car = pd.read_csv('car.csv')

sns.kdeplot(x='Age',fill=True,data=car)
plt.title("age of buying car first time")
plt.xlabel('age')
plt.ylabel('density')
plt.show()