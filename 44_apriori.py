'''
### Movie Recommendation Using Apriori
In this example, the Apriori algorithm is used to discover relationships between movies based on users' movie preferences. A real-world MovieLens dataset is used, where each user has rated multiple movies.
For association rule mining, movies with a sufficiently high rating are considered movies that the user **liked**. Each user's collection of liked movies is treated as a single transaction. Apriori then identifies frequently occurring combinations of movies and generates association rules based on their support, confidence, and lift.

For example, if many users who liked **Movie A** also liked **Movie B**, Apriori may generate the rule:

**Movie A → Movie B**

This rule can then be used to recommend **Movie B** to users who have shown interest in **Movie A**.

The objective of this example is to demonstrate how **Association Rule Learning can be applied to a real-world movie recommendation problem**.

dataset download link - https://grouplens.org/datasets/movielens/100k/
'''

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Load ratings
ratings = pd.read_csv(
    "ml-100k/u.data",
    sep="\t",
    names=["UserID", "MovieID", "Rating", "Timestamp"]
)

movies = pd.read_csv(
    "ml-100k/u.item",
    sep="|",
    encoding="latin-1",
    header=None,
    usecols=[0, 1],
    names=["MovieID", "MovieTitle"]
)
# Keep movies that users liked
liked = ratings[ratings["Rating"] >= 4]

# Add movie names
liked = liked.merge(
    movies,
    on="MovieID"
)

# Create one transaction for each user
transactions = (
    liked.groupby("UserID")["MovieTitle"]
    .apply(list)
    .tolist()
)
# print(transactions[0:5])
# exit(1)
# Convert transactions to binary format
encoder = TransactionEncoder()
data = encoder.fit_transform(transactions)
df = pd.DataFrame(data,columns=encoder.columns_)
print("NUMBER OF USERS:", len(transactions))
print("NUMBER OF MOVIES:", len(df.columns))
print(df.head())
# exit(1)
# Find frequent movie combinations
frequent_itemsets = apriori(df,min_support=0.05,use_colnames=True)
print("\nFREQUENT MOVIE ITEMSETS")
# print(frequent_itemsets)
# exit(1)
# Generate association rules
rules = association_rules(
    frequent_itemsets,
    metric="confidence",
    min_threshold=0.50
)

# Keep useful columns
rules = rules[
    [
        "antecedents",
        "consequents",
        "support",
        "confidence",
        "lift"
    ]
]

# Keep positive associations
rules = rules[rules["lift"] >= 1.5]
rules = rules[rules["consequents"].apply(lambda x: len(x) == 1)]

# ==========================================
# TASK 1: Remove duplicate entry, skip entry with lower confidence
# ==========================================

# 1. Create a column that takes the UNION of antecedents and consequents
rules['itemset_pair'] = rules.apply(
    lambda x: x['antecedents'].union(x['consequents']), axis=1
)

# 2. Sort by confidence (highest first)
filtered_rules = rules.sort_values(by='confidence', ascending=False)

# 3. Drop duplicates based on the unified itemset, keeping only the first (highest confidence)
filtered_rules = filtered_rules.drop_duplicates(subset=['itemset_pair'], keep='first')

# 4. Clean up the helper column and sort by lift for the final view
filtered_rules = filtered_rules.drop(columns=['itemset_pair']).sort_values(by='lift', ascending=False)

print("\nMOVIE ASSOCIATION RULES (AFTER REMOVING DUPLICATES)")

for _, rule in filtered_rules.head(20).iterrows():
    antecedent = ", ".join(rule["antecedents"])
    consequent = ", ".join(rule["consequents"])

    print(f"{antecedent} -> {consequent}")
    print(f"Support: {rule['support']:.2f}")
    print(f"Confidence: {rule['confidence']:.2f}")
    print(f"Lift: {rule['lift']:.2f}")
    print("-" * 50)


# ==========================================
# TASK 2: Export data into MySQL format 
# ==========================================

# 1. Convert frozensets to comma-separated strings for MySQL compatibility
filtered_rules['antecedents'] = filtered_rules['antecedents'].apply(lambda item: ', '.join(list(item)))
filtered_rules['consequents'] = filtered_rules['consequents'].apply(lambda item: ', '.join(list(item)))

# 2. Round the numerical metrics to an exact number of decimal places
numeric_columns = ['support', 'confidence', 'lift']
for col in numeric_columns:
    if col in filtered_rules.columns:
        filtered_rules[col] = filtered_rules[col].round(4)

# 3. Generate MySQL insert statements and save to a .sql file
file_name = "movie_recommendations.sql"
table_name = "movie_rules"

with open(file_name, "w", encoding="utf-8") as f:
    # Create table structure
    f.write(f"CREATE TABLE IF NOT EXISTS {table_name} (\n")
    f.write("    id INT AUTO_INCREMENT PRIMARY KEY,\n")
    f.write("    antecedents VARCHAR(255),\n")
    f.write("    consequents VARCHAR(255),\n")
    f.write("    support FLOAT,\n")
    f.write("    confidence FLOAT,\n")
    f.write("    lift FLOAT\n")
    f.write(");\n\n")

    # Write Insert Queries
    for _, row in filtered_rules.iterrows():
        # Escape single quotes for movie names (e.g. "Schindler's List" -> "Schindler''s List")
        ant = row['antecedents'].replace("'", "''")
        con = row['consequents'].replace("'", "''")
        
        insert_query = (
            f"INSERT INTO {table_name} (antecedents, consequents, support, confidence, lift) "
            f"VALUES ('{ant}', '{con}', {row['support']}, {row['confidence']}, {row['lift']});\n"
        )
        f.write(insert_query)

print(f"\nDuplicates removed and data successfully exported to {file_name}")