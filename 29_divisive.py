#4)  Organizing a Broad E-commerce CatalogScenario: An online retailer wants to take a massive "All Products" inventory and repeatedly split it into finer sub-categories.Input Features ($X$):$X_1$: Product weight (in kg)$X_2$: Average retail price (in USD)Target Variable ($Y$): Department sub-category (Cluster)Practice Goal: Split the master product list iteratively to form 3 distinct department categories based on physical size and cost.
# ============================================================
# DIVISIVE HIERARCHICAL CLUSTERING
# Example: Organizing an E-commerce Product Catalog
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
    "Product": [
        "Laptop",
        "Smartphone",
        "Refrigerator",
        "Washing Machine",
        "Headphones",
        "Microwave",
        "Office Chair",
        "Keyboard",
        "Television",
        "Blender",
        "Tablet",
        "Desk Lamp"
    ],

    # Product weight in kg
    "Product_weight": [
        2.0,
        0.2,
        65.0,
        55.0,
        0.3,
        12.0,
        15.0,
        0.8,
        10.0,
        3.0,
        0.6,
        1.5
    ],

    # Average retail price in USD
    "Average_price": [
        1000,
        700,
        1200,
        900,
        150,
        250,
        300,
        80,
        800,
        120,
        500,
        60
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
        "Product_weight",
        "Average_price"
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

def divisive_clustering(X, products, no_of_clusters=3):

    # Initially all products are in one cluster
    clusters = {
        0: list(range(len(products)))
    }

    next_key = 1

    # Continue until required number of clusters is reached
    while len(clusters) < no_of_clusters:

        # Find cluster with maximum number of products
        max_key = max(
            clusters,
            key=lambda cluster_id: len(clusters[cluster_id])
        )

        # Get indexes of products
        indexes = clusters[max_key]

        # Get data of selected cluster
        data = X[indexes]

        # Create KMeans model with 2 clusters
        model = KMeans(
            n_clusters=2,
            random_state=2,
            n_init=10
        )

        # Fit model
        model.fit_predict(data)

        # Get cluster labels
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
    df["Product"].to_list(),
    3
)

print(clusters)


# ============================================================
# Step 7: Display Cluster ID and Product Name
# ============================================================

for cluster_id, indexes in clusters.items():

    print("Cluster", cluster_id)

    for index in indexes:
        print(df.loc[index, "Product"])

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
    df["Product_weight"],
    df["Average_price"],
    c=df["cluster"],
    s=100
)


# Add labels for each product
for i in range(len(df)):

    plt.annotate(
        df.loc[i, "Product"],
        (
            df.loc[i, "Product_weight"],
            df.loc[i, "Average_price"]
        ),
        xytext=(5, 5),
        textcoords="offset points"
    )


plt.title("Divisive Clustering of E-commerce Products")

plt.xlabel("Product Weight (kg)")

plt.ylabel("Average Retail Price (USD)")

plt.show()