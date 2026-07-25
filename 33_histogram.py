1 #create Histogram chart for virat kohli ODI career 
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
run = pd.read_csv('ODI.csv')

# print(score)
sns.histplot(x='Year',data=run,kde=False,color='yellow',bins=10)
plt.xlabel('year')
plt.ylabel('score')
plt.title('virat kohli odi matches')
plt.show()
