#3) Genomic Sequence GroupingScenario: A biologist has individual DNA samples and wants to construct a phylogenetic tree by pairing the most genetically similar sequences step-by-step.Input Features ($X$):$X_1$: Genetic Marker A expression level$X_2$: Genetic Marker B expression levelTarget Variable ($Y$): Phylogenetic clade (Cluster)Practice Goal: Group samples bottom-up using Ward's linkage to find the evolutionary branches of the samples.
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
    "Sample": [
        "S1", "S2", "S3",
        "S4", "S5", "S6",
        "S7", "S8", "S9",
        "S10", "S11", "S12"
    ],

    "MarkerA": [
        1.2, 1.5, 1.8,
        5.4, 5.8, 6.1,
        9.2, 9.5, 9.8,
        1.4, 5.6, 9.4
    ],

    "MarkerB": [
        8.5, 8.8, 8.2,
        4.8, 5.2, 5.0,
        1.5, 1.8, 1.2,
        8.9, 5.1, 1.6
    ]
}

# create dataframe
df = pd.DataFrame(data)
# print(df)
#select input features
x = df[[
    "MarkerA",
    "MarkerB"
]]

print(x)

#data scale
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
print(x_scaled)

ward_linkage = linkage(x_scaled,method='ward')

plt.figure(figsize=(10,12))
#create dendrogram 
dendrogram(ward_linkage,labels=df["Sample"].values)

plt.title("Hierarchical Clustering Dendrogram - Ward Method")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.show()



model = AgglomerativeClustering(n_clusters=3,linkage="ward")
model.fit_predict(x_scaled)

print(model.labels_)
df['clusters'] = model.labels_
print(df)

#create chart
plt.figure(figsize=(10,8))
plt.title("agglomerative hierarchical clustering")
plt.scatter(df['MarkerA'],df['MarkerB'],c=df['clusters'])
plt.xlabel("Marker A Expression")
plt.ylabel("Marker B Expression")
#add label for each and every circle
for index in range(len(df)):
    plt.annotate(df.loc[index,'Sample'],(
        df.loc[index,'MarkerA'],
        df.loc[index,'MarkerB']
    ),xytext=(5,5),textcoords="offset points")
plt.show()
exit()