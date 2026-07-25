#create KDE chart of doing marriage 1st time in india 
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
person = pd.read_csv('marriage_india.csv')

sns.kdeplot(x='age',fill=True,data=person)
plt.title("age of marriage first time")
plt.xlabel('age')
plt.ylabel('density')
plt.show()