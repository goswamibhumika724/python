# 5 Agriculture Soil Fertility Grouping

# Features 4

#  Soil pH
#  Nitrogen mgkg
#  Phosphorus mgkg
#  Electrical Conductivity dSm

# Finding the value of k Elbow Method
# Run KMeans for k  1 to 7 and calculate WCSS The elbow appears at k  3

# Clusters k  3

#  Cluster 1  Poor Soil Low pH and low nitrogen and phosphorus The soil may need additional treatment

#  Cluster 2  Good Agricultural Soil Balanced pH with good levels of nitrogen and phosphorus

#  Cluster 3  Salty Soil High pH high phosphorus and high electrical conductivity The soil may have excess fertilizer or salt

import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

#create dataset 
X = np.array([ [5.2,25,15,0.4], [5.4,28,18,0.5], [5.1,22,12,0.3], [5.5,30,20,0.6], [5.3,26,16,0.4], [5.0,20,10,0.3], [5.6,32,22,0.5], [5.2,24,14,0.4], [5.4,27,17,0.5], [5.1,23,13,0.3], [6.5,70,45,0.8], [6.7,75,50,0.9], [6.4,68,42,0.7], [6.8,80,55,1.0], [6.6,72,48,0.8], [6.5,78,52,0.9], [6.9,82,58,1.1], [6.7,74,47,0.8], [6.3,65,40,0.7], [6.8,77,53,0.9], [7.8,85,90,2.5], [8.0,90,95,2.8], [7.7,82,88,2.4], [8.2,95,105,3.0], [7.9,88,92,2.7], [8.3,98,110,3.2], [7.6,80,85,2.3], [8.1,92,100,2.9], [7.8,86,94,2.6], [8.4,100,115,3.3], [5.3,27,17,0.4], [5.5,29,19,0.5], [5.2,24,14,0.3], [5.6,31,21,0.6], [5.1,21,11,0.3], [5.4,26,16,0.4], [5.7,33,23,0.5], [5.3,25,15,0.4], [5.5,28,18,0.5], [5.2,23,13,0.3], [6.6,73,46,0.8], [6.8,79,54,1.0], [6.4,67,41,0.7], [6.9,83,59,1.1], [6.5,71,47,0.8], [6.7,76,51,0.9], [6.3,64,39,0.7], [6.8,81,56,1.0], [6.6,69,44,0.8], [6.9,85,60,1.1] ])

model = KMeans(n_clusters=3,random_state=42,n_init=5)

#train model 
model.fit(X)

#extract labels
labels = model.labels_

#print(label)
print("labels = ",labels)

# print centeriods 
print(model.cluster_centers_)

#data 
soils = [ "Aarav","Aditi","Rohan","Priya","Arjun", "Neha","Rahul","Sneha","Vikram","Pooja", "Karan","Ananya","Rajesh","Kavita","Amit", "Nisha","Suresh","Riya","Manish","Divya", "Akash","Simran","Nitin","Pallavi","Ravi", "Shreya","Vivek","Isha","Sanjay","Meera", "Harsh","Komal","Deepak","Swati","Yash", "Tanvi","Prakash","Anjali","Mohit","Payal", "Abhishek","Kajal","Rakesh","Mansi","Dhruv", "Sonal","Pankaj","Bhavna","Kunal","Radhika" ]

for soil,data,label in zip(soils,X,labels): 
    print(f"Name : {soil} data = {data} label = {label}")

#create chart
plt.scatter(labels,X[:,0],s=10)
plt.xticks(ticks=range(0,3),labels=range(0,3))
plt.ylabel("soil pH")
plt.xlabel("Labels")
plt.show()

