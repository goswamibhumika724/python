# create boxplot chart using seaborn use sample data from seaborn
# -----------------------------------------------------------------
# 1) attention
# 2) diamonds
# 3) penguins
# 4) titanic

import seaborn as sns 
import matplotlib.pyplot as plt 

titanic = sns.load_dataset('titanic')
sns.boxplot(x='class',y='age',data=titanic)
plt.show()