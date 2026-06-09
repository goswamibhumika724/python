import matplotlib.pyplot as plt
import pandas as pd



covid = pd.read_csv("covid.csv.csv")

covid.columns = covid.columns.str.strip()

unique_cats = covid["categ"].unique()
print("Unique categories found:", unique_cats)

plt.figure(figsize=(10, 6))
plt.hexbin(covid["Sno"], covid["age"], gridsize=30, cmap="Blues")

plt.colorbar(label="Count in bin")
plt.xlabel("Serial Number (Sno)")
plt.ylabel("Age")
plt.title("Hexbin Plot of Covid Data")

plt.show()

