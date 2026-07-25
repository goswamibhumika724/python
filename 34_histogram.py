#create Histogram chart for Steave smith ODI career 
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
run = pd.read_csv('ODI_2.csv')

# print(score)
sns.histplot(x='Year',data=run,kde=False,color='blue',bins=10)
plt.xlabel('year')
plt.ylabel('score')
plt.title('steave smith odi matches')
plt.show()
