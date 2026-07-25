# create boxplot chart using seaborn use sample data from seaborn
# -----------------------------------------------------------------
# 1) attention
# 2) diamonds
# 3) penguins
# 4) titanic

import seaborn as sns 
import matplotlib.pyplot as plt 

diamonds = sns.load_dataset('diamonds')
sns.boxplot(x='cut',y='price',data=diamonds)
plt.show()