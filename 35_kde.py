#create KDE chart of buying IPhone 1st time 
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
iphone = pd.read_csv('iphone.csv')

sns.kdeplot(x='Age',fill=True,data=iphone)
plt.title("age of buying iphone first time")
plt.xlabel('age')
plt.ylabel('density')
plt.show()



