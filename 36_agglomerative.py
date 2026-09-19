#5) Topic Modeling for News ArticlesScenario: A news aggregator starts with individual articles and merges them into progressively larger overarching topics (e.g., individual tech articles merged into a general "Technology" category).Input Features ($X$):$X_1$: Keyword frequency count for "Economy"$X_2$: Keyword frequency count for "Election"Target Variable ($Y$): Broad news category (Cluster)Practice Goal: Compute a distance matrix and group the articles bottom-up to form 2 main news categories.
# Agglomerative Clustering (Bottom-Up)

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

# ============================================
# 1. Create customer dataset
# ============================================

data = {
    "Article": [
        "A1", "A2", "A3",
        "A4", "A5", "A6",
        "A7", "A8", "A9",
        "A10", "A11", "A12"
    ],

    "EconomyCount": [
        18, 22, 20,
        25, 19, 23,
        2, 4, 3,
        1, 5, 2
    ],

    "ElectionCount": [
        3, 2, 4,
        1, 5, 3,
        24, 20, 22,
        28, 25, 21
    ]
}

# create dataframe
df = pd.DataFrame(data)
# print(df)
#select input features
x = df[[
    "EconomyCount",
    "ElectionCount"
]]

print(x)

#data scale
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
print(x_scaled)

ward_linkage = linkage(x_scaled,method='ward')

plt.figure(figsize=(10,12))
#create dendrogram 
dendrogram(ward_linkage,labels=df["Article"].values)

plt.title("Hierarchical Clustering Dendrogram - Ward Method")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.show()



model = AgglomerativeClustering(n_clusters=2,linkage="ward")
model.fit_predict(x_scaled)

print(model.labels_)
df['clusters'] = model.labels_
print(df)

#create chart
plt.figure(figsize=(10,8))
plt.title("agglomerative hierarchical clustering")
plt.scatter(df['EconomyCount'],df['ElectionCount'],c=df['clusters'])
plt.xlabel("Keyword Count: Economy")
plt.ylabel("Keyword Count: Election")
#add label for each and every circle
for index in range(len(df)):
    plt.annotate(df.loc[index,'Article'],(
        df.loc[index,'EconomyCount'],
        df.loc[index,'ElectionCount']
    ),xytext=(5,5),textcoords="offset points")
plt.show()
exit()