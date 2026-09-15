# 10 Environmental Science Air Quality Zone Grouping

# Features 3

#  PM25 gm
#  Nitrogen Dioxide NO
#  Ozone O

# Clusters k  3

#  Cluster 1  Traffic Pollution Areas High NO and PM25 levels mainly because of vehicle traffic

#  Cluster 2  Smog Areas High ozone and PM25 levels usually found in sunny and polluted areas

#  Cluster 3  Clean Areas Low PM25 and NO levels usually found near parks or green areas

import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

# create dataset 
X = np.array([ [80,70,40], [75,65,42], [90,80,38], [85,75,45], [95,85,40], [70,60,35], [88,72,43], [92,78,39], [78,68,41], [100,88,37], [82,74,44], [87,76,40], [73,63,36], [96,82,42], [84,71,45], [91,79,38], [77,66,43], [89,73,41], [94,84,39], [81,69,44], [90,35,120], [100,40,135], [110,45,150], [85,32,125], [105,38,140], [115,42,155], [95,36,130], [120,48,160], [88,34,118], [108,41,145], [98,37,132], [112,44,152], [92,35,128], [118,46,158], [102,39,138], [125,50,165], [87,33,122], [107,40,142], [114,43,148], [97,36,134], [12,15,30], [15,18,28], [10,12,25], [18,20,32], [14,16,27], [20,22,35], [11,14,24], [16,19,31], [13,15,26], [19,21,34], [9,11,23], [17,18,29], [14,17,28], [21,23,36], [12,13,25], [16,20,30], [10,14,24], [18,19,32], [13,16,27], [15,18,29] ])

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
zones = [ "Zone1", "Zone2", "Zone3", "Zone4", "Zone5", "Zone6", "Zone7", "Zone8", "Zone9", "Zone10", "Zone11", "Zone12", "Zone13", "Zone14", "Zone15", "Zone16", "Zone17", "Zone18", "Zone19", "Zone20", "Zone21", "Zone22", "Zone23", "Zone24", "Zone25", "Zone26", "Zone27", "Zone28", "Zone29", "Zone30", "Zone31", "Zone32", "Zone33", "Zone34", "Zone35", "Zone36", "Zone37", "Zone38", "Zone39", "Zone40", "Zone41", "Zone42", "Zone43", "Zone44", "Zone45", "Zone46", "Zone47", "Zone48", "Zone49", "Zone50", "Zone51", "Zone52", "Zone53", "Zone54", "Zone55", "Zone56", "Zone57", "Zone58", "Zone59", "Zone60" ]

for zone, data, label in zip(zones,X,labels): 
    print(f"Name : {zone} data = {data} label = {label}")

#create chart
plt.scatter(labels,X[:,0],s=10)
plt.xticks(ticks=range(0,3),labels=range(0,3))
plt.ylabel("PM25 (gm)")
plt.xlabel("Labels")
plt.show()

