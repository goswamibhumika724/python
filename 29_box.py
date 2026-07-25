# create boxplot chart using seaborn use sample data from seaborn
# -----------------------------------------------------------------
# 1) attention
# 2) diamonds
# 3) penguins
# 4) titanic

import seaborn as sns 
import matplotlib.pyplot as plt 

attention = sns.load_dataset('attention')
sns.boxplot(x='attention',y='score',data=attention)
plt.show()