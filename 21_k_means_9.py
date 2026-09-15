# 8 Banking Credit Card Transaction Grouping

# Features 4

#  Transaction Amount 
#  Time Since Previous Transaction seconds
#  Distance from Usual Location km
#  POS Entry Mode

# Clusters k  4

#  Cluster 1  Normal Transactions Small or medium transactions made at regular intervals and familiar locations

#  Cluster 2  Travel Transactions Larger transactions made far away from the customers usual location

#  Cluster 3  Card Testing Very small transactions made repeatedly in a short period

#  Cluster 4  Suspicious Transactions Large transactions made quickly from unusual locations or using manual entry

import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

# create dataset 
X = np.array([ [50,3600,2,1], [75,4200,3,1], [120,3000,5,2], [90,3900,4,1], [60,4500,2,2], [150,3300,6,1], [80,4000,3,2], [110,3700,5,1], [45,4800,2,1], [130,3500,4,2], [70,4100,3,1], [100,3800,5,2], [55,4300,2,1], [140,3200,6,2], [85,4400,4,1], [500,7200,250,2], [750,9000,400,1], [1200,10800,600,2], [650,8400,350,1], [900,9600,500,2], [1100,12000,700,1], [800,7800,300,2], [1300,10200,650,1], [700,8700,450,2], [950,9900,550,1], [600,8100,320,2], [1000,11400,580,1], [850,9300,420,2], [1250,10500,620,1], [550,7500,280,2], [2,120,1,1], [5,180,2,1], [3,90,1,2], [1,150,2,1], [4,100,1,2], [6,200,2,1], [2,80,1,1], [5,130,2,2], [3,110,1,1], [4,160,2,1], [2,140,1,2], [6,170,2,1], [1,95,1,1], [5,125,2,2], [3,105,1,1], [1500,300,800,3], [2200,450,1000,3], [1800,600,750,4], [2500,350,1200,3], [1700,500,900,4], [3000,700,1500,3], [2000,400,1100,4], [2800,550,1300,3], [1600,250,850,4], [2400,650,1400,3], [1900,320,950,4], [2700,480,1250,3], [2100,580,1050,4], [3200,750,1600,3], [2300,380,1150,4] ])

model = KMeans(n_clusters=4,random_state=42,n_init=5)

#train model 
model.fit(X)

#extract labels
labels = model.labels_

#print(label)
print("labels = ",labels)

# print centroids
print(model.cluster_centers_)

# data names 
transactions = [ "Transaction1", "Transaction2", "Transaction3", "Transaction4", "Transaction5", "Transaction6", "Transaction7", "Transaction8", "Transaction9", "Transaction10", "Transaction11", "Transaction12", "Transaction13", "Transaction14", "Transaction15", "Transaction16", "Transaction17", "Transaction18", "Transaction19", "Transaction20", "Transaction21", "Transaction22", "Transaction23", "Transaction24", "Transaction25", "Transaction26", "Transaction27", "Transaction28", "Transaction29", "Transaction30", "Transaction31", "Transaction32", "Transaction33", "Transaction34", "Transaction35", "Transaction36", "Transaction37", "Transaction38", "Transaction39", "Transaction40", "Transaction41", "Transaction42", "Transaction43", "Transaction44", "Transaction45", "Transaction46", "Transaction47", "Transaction48", "Transaction49", "Transaction50", "Transaction51", "Transaction52", "Transaction53", "Transaction54", "Transaction55", "Transaction56", "Transaction57", "Transaction58", "Transaction59", "Transaction60" ]

for transaction, data, label in zip(transactions,X,labels): 
    print(f"Name : {transaction} data = {data} label = {label}")

#create chart
plt.scatter(labels,X[:,0],s=10)
plt.xticks(ticks=range(0,4),labels=range(0,4))
plt.ylabel("Transaction Amount")
plt.xlabel("Labels")
plt.show()
