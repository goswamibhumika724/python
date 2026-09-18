# ------------------------------------------------------
# Divisive Clustering (Top-Down)
# ------------------------------------------------------

# 1) Macro-Market SplittingScenario: A global streaming service wants to divide its single massive global user base into distinct regional cohorts by repeatedly splitting the largest, most diverse groups.Input Features ($X$):$X_1$: Average daily watch time (in minutes)$X_2$: Preference score for localized content (1-10)Target Variable ($Y$): Regional cohort grouping (Cluster)Practice Goal: Start with all users in one cluster and split them top-down to find 2 highly cohesive viewer markets.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    "User_ID": [
        "User_01", "User_02", "User_03", "User_04", "User_05", "User_06",
        "User_07", "User_08", "User_09", "User_10", "User_11", "User_12"
    ],
    "Daily_watch_time": [
        45, 180, 210, 60, 240, 50, 195, 75, 230, 65, 170, 55
    ],
    "Local_content_preference": [
        2, 8, 9, 3, 8, 1, 7, 4, 9, 2, 8, 3
    ]
}

df = pd.DataFrame(data)

X = df[["Daily_watch_time", "Local_content_preference"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

def divisive_clustering(X, users, no_of_clusters=3):
    clusters = {
        0: list(range(len(users)))
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

clusters = divisive_clustering(X_scaled, df['User_ID'].to_list(), 3)
print(clusters)

for cluster_id, indexes in clusters.items():
    print(cluster_id)
    for index in indexes:
        print(df.loc[index, "User_ID"])

df['cluster'] = 0
for cluster_id, indexes in clusters.items():
    print(cluster_id)
    for index in indexes:
        df.loc[index, "cluster"] = cluster_id

print(df)

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Daily_watch_time"],
    df["Local_content_preference"],
    c=df["cluster"],
    s=100
)

for cluster in range(len(df)):
    plt.annotate(
        df.loc[cluster, "User_ID"],
        (
            df.loc[cluster, "Daily_watch_time"],
            df.loc[cluster, "Local_content_preference"]
        ),
        xytext=(5, 5),
        textcoords="offset points"
    )

plt.xlabel("Average Daily Watch Time (Minutes)")
plt.ylabel("Preference for Localized Content (1-10)")
plt.title("Divisive Hierarchical Clustering: Streaming Market Cohorts")

plt.show()
