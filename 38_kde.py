#create KDE chart of taking divorce in which year after marriage.
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
person = pd.read_csv('divorce.csv')

sns.kdeplot(x='Years_After_Marriage',fill=True,data=person)
plt.title("age of taking divorce")
plt.xlabel('age')
plt.ylabel('density')
plt.show()