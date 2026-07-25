# create boxplot chart using seaborn use sample data from seaborn
# -----------------------------------------------------------------
# 1) attention
# 2) diamonds
# 3) penguins
# 4) titanic

import seaborn as sns 
import matplotlib.pyplot as plt 

penguins = sns.load_dataset('penguins')
sns.boxplot(x='island',y='body_mass_g',data=penguins)
plt.show()