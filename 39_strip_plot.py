#create strip_plot chart of runs scored by different team in ipl since 2008
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
score = pd.read_csv('ipl.csv')
print(score)
sns.stripplot(data=score,x='Team',y='Runs',jitter=True)
plt.xlabel('team')
plt.ylabel('run scored')
plt.title("ipl team wise score")
plt.show()