#4) Factory Machine Failure ModesScenario: An engineer wants to group individual machine breakdown incidents to find common root causes by linking the most similar failure metrics first.Input Features ($X$):$X_1$: Operating temperature at time of failure (in Celsius)$X_2$: Vibration frequency anomaly (in Hz)Target Variable ($Y$): Failure mode prototype (Cluster)Practice Goal: Use bottom-up clustering to merge incidents until 3 distinct types of machine failure modes are identified.
# Agglomerative Clustering (Bottom-Up)

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

# ============================================
# 1. Create machine incident dataset
# ============================================

data = {
    "Incident": [
        "M1", "M2", "M3",
        "M4", "M5", "M6",
        "M7", "M8", "M9",
        "M10", "M11", "M12"
    ],

    "Temperature": [
        95, 98, 102,
        45, 48, 50,
        88, 92, 90,
        96, 47, 89
    ],

    "VibrationHz": [
        15, 18, 12,
        85, 90, 88,
        78, 82, 80,
        14, 86, 79
    ]
}

# create dataframe
df = pd.DataFrame(data)
# print(df)
#select input features
x = df[[
    "Temperature",
    "VibrationHz"
]]

print(x)

#data scale
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
print(x_scaled)

ward_linkage = linkage(x_scaled,method='ward')

plt.figure(figsize=(10,12))
#create dendrogram 
dendrogram(ward_linkage,labels=df["Incident"].values)

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
plt.scatter(df['Temperature'],df['VibrationHz'],c=df['clusters'])
plt.xlabel("Operating Temperature (°C)")
plt.ylabel("Vibration Frequency Anomaly (Hz)")
#add label for each and every circle
for index in range(len(df)):
    plt.annotate(df.loc[index,'Incident'],(
        df.loc[index,'Temperature'],
        df.loc[index,'VibrationHz']
    ),xytext=(5,5),textcoords="offset points")
plt.show()
exit()