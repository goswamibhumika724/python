#5) Network Traffic Anomaly SegregationScenario: A cybersecurity system logs all incoming server traffic as one large dataset and needs to split it sequentially to isolate normal traffic from distinct types of DDoS attacks.Input Features ($X$):$X_1$: Requests per second from source IP$X_2$: Average packet size (in bytes)Target Variable ($Y$): Traffic classification group (Cluster)Practice Goal: Isolate malicious traffic by continuously splitting the most anomalous subgroups top-down until the "normal" baseline is separated from the attacks.
# ============================================================
# DIVISIVE HIERARCHICAL CLUSTERING
# Example: Network Traffic Anomaly Segregation
# ============================================================

# Step 1: Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# ============================================================
# Step 2: Create the dataset
# ============================================================

data = {
    "Traffic": [
        "Normal_1",
        "Normal_2",
        "Normal_3",
        "Normal_4",
        "Normal_5",
        "HTTP_Flood_1",
        "HTTP_Flood_2",
        "HTTP_Flood_3",
        "UDP_Flood_1",
        "UDP_Flood_2",
        "UDP_Flood_3",
        "SYN_Flood_1",
        "SYN_Flood_2",
        "SYN_Flood_3"
    ],

    # Requests per second from source IP
    "Requests_per_second": [
        20,
        25,
        30,
        35,
        28,
        500,
        550,
        600,
        900,
        950,
        1000,
        700,
        750,
        800
    ],

    # Average packet size in bytes
    "Average_packet_size": [
        500,
        520,
        480,
        510,
        495,
        800,
        850,
        820,
        200,
        220,
        210,
        600,
        620,
        610
    ]
}


# Create dataframe
df = pd.DataFrame(data)

# print(df)


# ============================================================
# Step 3: Select input features
# ============================================================

X = df[
    [
        "Requests_per_second",
        "Average_packet_size"
    ]
]


# ============================================================
# Step 4: Scaling
# ============================================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# print(X_scaled)


# ============================================================
# Step 5: Divisive Clustering Function
# ============================================================

def divisive_clustering(X, traffic, no_of_clusters=4):

    # Initially all traffic is in one cluster
    clusters = {
        0: list(range(len(traffic)))
    }

    next_key = 1

    # Continue until required number of clusters is reached
    while len(clusters) < no_of_clusters:

        # Find cluster with maximum number of records
        max_key = max(
            clusters,
            key=lambda cluster_id: len(clusters[cluster_id])
        )

        # Get indexes
        indexes = clusters[max_key]

        # Get data
        data = X[indexes]

        # Create KMeans model with 2 clusters
        model = KMeans(
            n_clusters=2,
            random_state=2,
            n_init=10
        )

        # Fit model
        model.fit_predict(data)

        # Get labels
        labels = model.labels_

        # Create two lists
        list_1 = []
        list_2 = []

        for index, label in zip(indexes, labels):

            if label == 0:
                list_1.append(index)

            else:
                list_2.append(index)

        # Add new clusters
        clusters[next_key] = list_1
        next_key = next_key + 1

        clusters[next_key] = list_2
        next_key = next_key + 1

        # Delete old cluster
        del clusters[max_key]

    return clusters


# ============================================================
# Step 6: Apply Divisive Clustering
# ============================================================

clusters = divisive_clustering(
    X_scaled,
    df["Traffic"].to_list(),
    4
)

print(clusters)


# ============================================================
# Step 7: Display Cluster ID and Traffic Type
# ============================================================

for cluster_id, indexes in clusters.items():

    print("Cluster", cluster_id)

    for index in indexes:
        print(df.loc[index, "Traffic"])

    print()


# ============================================================
# Step 8: Add Cluster Column to Original DataFrame
# ============================================================

df["cluster"] = 0

# Add cluster data into original dataframe
for cluster_id, indexes in clusters.items():

    for index in indexes:

        df.loc[index, "cluster"] = cluster_id


# Display final dataframe
print(df)


# ============================================================
# Step 9: Display Data as Chart
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Requests_per_second"],
    df["Average_packet_size"],
    c=df["cluster"],
    s=100
)


# Add labels for each traffic record
for i in range(len(df)):

    plt.annotate(
        df.loc[i, "Traffic"],
        (
            df.loc[i, "Requests_per_second"],
            df.loc[i, "Average_packet_size"]
        ),
        xytext=(5, 5),
        textcoords="offset points"
    )


plt.title("Divisive Clustering of Network Traffic")

plt.xlabel("Requests per Second")

plt.ylabel("Average Packet Size (Bytes)")

plt.show()