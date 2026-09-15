#  9 Sports Analytics Football Midfielder Grouping

# Features 3

#  Progressive Passes per 90 minutes
#  Defensive Pressures per 90 minutes
#  Distance Covered kmmatch

# Finding the value of k
# We choose k  3 because midfielders can be grouped into three common playing styles

# Clusters k  3

#  Cluster 1  Playmakers Make many forward passes but apply less defensive pressure

#  Cluster 2  Defensive Midfielders Make fewer forward passes but apply strong defensive pressure

#  Cluster 3  BoxtoBox Players Contribute in both attack and defence and cover a large distance

import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

# create dataset 
X = np.array([ [8,4,9.5], [10,5,10.2], [12,4,9.8], [9,6,10.0], [11,5,10.5], [13,4,9.7], [10,6,10.1], [14,5,10.3], [9,4,9.6], [12,6,10.4], [11,4,9.9], [15,5,10.6], [10,5,9.8], [13,6,10.2], [12,4,10.0], [14,5,10.5], [11,6,9.7], [15,4,10.3], [13,5,10.1], [10,4,9.9], [4,12,10.0], [5,14,10.3], [6,16,10.1], [3,13,9.8], [7,15,10.5], [5,17,10.2], [4,14,9.9], [6,18,10.4], [3,16,10.0], [7,13,10.6], [5,15,10.1], [4,17,10.3], [6,14,9.7], [5,16,10.2], [7,18,10.5], [4,15,10.0], [6,17,10.4], [5,13,9.9], [3,14,10.1], [7,16,10.3], [10,10,11.5], [12,11,12.0], [9,12,11.8], [13,10,12.3], [11,13,12.1], [14,12,12.5], [10,14,11.9], [15,11,12.4], [12,13,12.2], [9,11,11.7], [13,14,12.6], [11,10,11.6], [14,13,12.3], [10,12,12.0], [15,14,12.7], [12,10,11.9], [13,12,12.5], [11,14,12.1], [14,11,12.4], [10,13,11.8] ])

model = KMeans(n_clusters=3,random_state=42,n_init=5)

#train model 
model.fit(X)

#extract labels
labels = model.labels_

#print(label)
print("labels = ",labels)

# print centroids 
print(model.cluster_centers_)

# data names 
players = [ "Player1", "Player2", "Player3", "Player4", "Player5", "Player6", "Player7", "Player8", "Player9", "Player10", "Player11", "Player12", "Player13", "Player14", "Player15", "Player16", "Player17", "Player18", "Player19", "Player20", "Player21", "Player22", "Player23", "Player24", "Player25", "Player26", "Player27", "Player28", "Player29", "Player30", "Player31", "Player32", "Player33", "Player34", "Player35", "Player36", "Player37", "Player38", "Player39", "Player40", "Player41", "Player42", "Player43", "Player44", "Player45", "Player46", "Player47", "Player48", "Player49", "Player50", "Player51", "Player52", "Player53", "Player54", "Player55", "Player56", "Player57", "Player58", "Player59", "Player60" ]

for player, data, label in zip(players,X,labels): 
    print(f"Name : {player} data = {data} label = {label}")

#create chart
plt.scatter(labels,X[:,0],s=10)
plt.xticks(ticks=range(0,3),labels=range(0,3))
plt.ylabel("Progressive Passes per 90 minutes")
plt.xlabel("Labels")
plt.show()

