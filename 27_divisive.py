#2) Supply Chain Logistics HubsScenario: A national delivery company wants to split a massive country-wide delivery zone into smaller, localized fulfillment regions to reduce shipping times.Input Features ($X$):$X_1$: Delivery coordinate (Latitude)$X_2$: Delivery coordinate (Longitude)Target Variable ($Y$): Assigned localized logistics region (Cluster)Practice Goal: Divide the entire national map top-down into 3 sub-regions by continually splitting the cluster with the highest spatial variance.
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    "Hub": [
        "Hub_01", "Hub_02", "Hub_03", "Hub_04", "Hub_05", "Hub_06",
        "Hub_07", "Hub_08", "Hub_09", "Hub_10", "Hub_11", "Hub_12"
    ],
    "Latitude": [
        28.61, 31.10, 26.20, 19.07, 15.50, 22.30,
        13.08, 9.93, 11.01, 26.91, 17.38, 22.57
    ],
    "Longitude": [
        77.20, 75.34, 78.15, 72.87, 73.80, 70.80,
        80.27, 76.27, 76.95, 75.78, 78.48, 88.36
    ]
}

df = pd.DataFrame(data)

X = df[["Latitude", "Longitude"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

def divisive_clustering(X, hubs, no_of_clusters=3):
    clusters = {
        0: list(range(len(hubs)))
    }
    next_key = 1
    while len(clusters) < no_of_clusters:
        max_key = max(clusters, key=lambda cluster_id: len(clusters[cluster_id]))
        indexes = clusters[max_key]
        data = X[indexes]
        
        model = KMeans(n_clusters=2, random_state=2, n_init=10)
        model.fit_predict(data)
        labels = model.labels_
        
        list_1 = []
        list_2 = []
        for index, label in zip(indexes, labels):
            if label == 0:
                list_1.append(index)
            else:
                list_2.append(index)
                
        clusters[next_key] = list_1
        next_key = next_key + 1
        clusters[next_key] = list_2
        next_key = next_key + 1
        del clusters[max_key]
        
    return clusters

clusters = divisive_clustering(X_scaled, df['Hub'].to_list(), 3)
print(clusters)

for cluster_id, indexes in clusters.items():
    print(cluster_id)
    for index in indexes:
        print(df.loc[index, "Hub"])

df['cluster'] = 0
for cluster_id, indexes in clusters.items():
    print(cluster_id)
    for index in indexes:
        df.loc[index, "cluster"] = cluster_id

print(df)

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Longitude"],
    df["Latitude"],
    c=df["cluster"],
    s=100
)

for cluster in range(len(df)):
    plt.annotate(
        df.loc[cluster, "Hub"],
        (
            df.loc[cluster, "Longitude"],
            df.loc[cluster, "Latitude"]
        ),
        xytext=(5, 5),
        textcoords="offset points"
    )

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Divisive Hierarchical Clustering: Supply Chain Logistics Hubs")

plt.show()

