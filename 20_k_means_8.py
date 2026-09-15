# 7 Manufacturing Machine Bearing Condition

# Features 2

#  Vibration Level g
#  Operating Temperature C

# Clusters k  3

#  Cluster 1  Healthy Machine Low vibration and normal operating temperature

#  Cluster 2  Machine Wear Higher vibration and temperature which may indicate mechanical problems

#  Cluster 3  Critical Condition Very high vibration and temperature indicating that the machine may fail soon

import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

# create dataset 
X = np.array([ [0.20,45], [0.25,47], [0.18,44], [0.30,48], [0.22,46], [0.27,49], [0.19,45], [0.24,47], [0.21,46], [0.28,48], [0.23,45], [0.26,47], [0.17,43], [0.29,49], [0.20,44], [0.25,46], [0.22,47], [0.18,45], [0.27,48], [0.24,46], [0.80,60], [0.90,62], [0.75,58], [1.00,65], [0.85,61], [0.95,63], [0.70,57], [1.05,66], [0.88,60], [0.92,64], [0.78,59], [1.10,67], [0.82,61], [0.98,65], [0.73,58], [0.87,62], [1.02,66], [0.79,60], [0.91,63], [0.84,61], [1.80,80], [2.00,85], [1.70,78], [2.20,88], [1.90,82], [2.10,86], [1.75,79], [2.30,90], [1.85,81], [2.05,84], [1.95,83], [2.40,92], [1.65,77], [2.15,87], [1.88,82], [2.25,89], [1.72,80], [2.35,91], [1.98,84], [2.12,86] ])

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
machines = [ "Machine1", "Machine2", "Machine3", "Machine4", "Machine5", "Machine6", "Machine7", "Machine8", "Machine9", "Machine10", "Machine11", "Machine12", "Machine13", "Machine14", "Machine15", "Machine16", "Machine17", "Machine18", "Machine19", "Machine20", "Machine21", "Machine22", "Machine23", "Machine24", "Machine25", "Machine26", "Machine27", "Machine28", "Machine29", "Machine30", "Machine31", "Machine32", "Machine33", "Machine34", "Machine35", "Machine36", "Machine37", "Machine38", "Machine39", "Machine40", "Machine41", "Machine42", "Machine43", "Machine44", "Machine45", "Machine46", "Machine47", "Machine48", "Machine49", "Machine50", "Machine51", "Machine52", "Machine53", "Machine54", "Machine55", "Machine56", "Machine57", "Machine58", "Machine59", "Machine60" ]

for machine, data, label in zip(machines,X,labels): 
    print(f"Name : {machine} data = {data} label = {label}")

#create chart
plt.scatter(labels,X[:,0],s=10)
plt.xticks(ticks=range(0,3),labels=range(0,3))
plt.ylabel("Vibration Level (g)")
plt.xlabel("Labels")
plt.show()
