#3) Codebase Microservices RefactoringScenario: A software architect needs to break down a giant monolithic application into smaller microservices by separating distinct functional modules.Input Features ($X$):$X_1$: Number of shared database tables utilized$X_2$: Frequency of cross-module API calls per minuteTarget Variable ($Y$): Microservice boundary (Cluster)Practice Goal: Partition the monolith top-down into 2 independent microservices with minimal overlap.
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    "Module": [
        "Auth", "Billing", "Notification", "Catalog", "Search", "Inventory",
        "Cart", "Checkout", "Reporting", "Analytics", "Shipping", "Reviews"
    ],
    "Shared_DB_Tables": [
        2, 9, 3, 1, 2, 8,
        7, 10, 3, 2, 7, 1
    ],
    "Cross_Module_API_Calls": [
        15, 120, 25, 10, 30, 110,
        95, 130, 35, 20, 100, 15
    ]
}

df = pd.DataFrame(data)

X = df[["Shared_DB_Tables", "Cross_Module_API_Calls"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

def divisive_clustering(X, modules, no_of_clusters=2):
    clusters = {
        0: list(range(len(modules)))
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

clusters = divisive_clustering(X_scaled, df['Module'].to_list(), 2)
print(clusters)

for cluster_id, indexes in clusters.items():
    print(cluster_id)
    for index in indexes:
        print(df.loc[index, "Module"])

df['cluster'] = 0
for cluster_id, indexes in clusters.items():
    print(cluster_id)
    for index in indexes:
        df.loc[index, "cluster"] = cluster_id

print(df)

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Shared_DB_Tables"],
    df["Cross_Module_API_Calls"],
    c=df["cluster"],
    s=100
)

for cluster in range(len(df)):
    plt.annotate(
        df.loc[cluster, "Module"],
        (
            df.loc[cluster, "Shared_DB_Tables"],
            df.loc[cluster, "Cross_Module_API_Calls"]
        ),
        xytext=(5, 5),
        textcoords="offset points"
    )

plt.xlabel("Shared Database Tables")
plt.ylabel("Cross-Module API Calls Per Minute")
plt.title("Divisive Hierarchical Clustering: Codebase Microservices Refactoring")

plt.show()