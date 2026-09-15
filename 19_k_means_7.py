#  6 Cybersecurity Network Traffic Grouping

# Features 3

#  Packet Frequency packetssec
#  Average Packet Size bytes
#  Unique Destination IP Ratio

# Finding the value of k
# We choose k  3 to separate normal network traffic from two common types of unusual traffic

# Clusters k  3

#  Cluster 1  Normal Traffic Normal packet frequency with different packet sizes and normal IP usage

#  Cluster 2  Port Scanning Many packets are sent to different IP addresses usually with small and similar packet sizes

#  Cluster 3  Heavy Data Transfer Large packets are sent repeatedly usually to one main destination

import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

# create dataset 
X = np.array([ [20,450,0.30], [22,500,0.35], [18,420,0.25], [25,550,0.40], [21,480,0.32], [19,460,0.28], [24,520,0.38], [23,490,0.34], [20,470,0.30], [22,510,0.36], [26,560,0.42], [17,400,0.22], [21,455,0.31], [24,530,0.37], [19,440,0.27], [23,515,0.35], [25,540,0.39], [18,430,0.24], [22,495,0.33], [20,465,0.29], [150,100,0.90], [180,110,0.95], [200,90,0.98], [170,105,0.92], [220,95,0.99], [160,115,0.91], [190,100,0.96], [210,85,0.99], [175,108,0.94], [205,92,0.97], [155,102,0.89], [185,98,0.95], [215,88,0.98], [165,112,0.93], [195,96,0.97], [225,90,0.99], [172,104,0.92], [202,94,0.96], [188,101,0.95], [218,87,0.98], [40,1400,0.10], [45,1500,0.12], [38,1350,0.08], [50,1600,0.15], [42,1450,0.11], [48,1550,0.13], [35,1300,0.07], [46,1480,0.10], [44,1520,0.12], [52,1650,0.16], [39,1380,0.09], [47,1500,0.11], [41,1420,0.10], [53,1700,0.17], [36,1320,0.08], [49,1580,0.14], [43,1460,0.11], [51,1620,0.15], [37,1340,0.09], [45,1510,0.12] ])

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
traffic = [ "Traffic1", "Traffic2", "Traffic3", "Traffic4", "Traffic5", "Traffic6", "Traffic7", "Traffic8", "Traffic9", "Traffic10", "Traffic11", "Traffic12", "Traffic13", "Traffic14", "Traffic15", "Traffic16", "Traffic17", "Traffic18", "Traffic19", "Traffic20", "Traffic21", "Traffic22", "Traffic23", "Traffic24", "Traffic25", "Traffic26", "Traffic27", "Traffic28", "Traffic29", "Traffic30", "Traffic31", "Traffic32", "Traffic33", "Traffic34", "Traffic35", "Traffic36", "Traffic37", "Traffic38", "Traffic39", "Traffic40", "Traffic41", "Traffic42", "Traffic43", "Traffic44", "Traffic45", "Traffic46", "Traffic47", "Traffic48", "Traffic49", "Traffic50", "Traffic51", "Traffic52", "Traffic53", "Traffic54", "Traffic55", "Traffic56", "Traffic57", "Traffic58", "Traffic59", "Traffic60" ]

for traffic_name, data, label in zip(traffic, X, labels): 
    print( f"Name : {traffic_name} data = {data} label = {label}" )

#create chart
plt.scatter(labels,X[:,0],s=10)
plt.xticks(ticks=range(0,3),labels=range(0,3))
plt.ylabel("Packet Frequency (packets/sec)")
plt.xlabel("Labels")
plt.show()

