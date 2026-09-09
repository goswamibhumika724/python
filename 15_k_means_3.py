# 2 Healthcare Patient Risk Grouping

# Features 3

#  Systolic Blood Pressure mmHg
#  Fasting Blood Glucose mgdL
#  LDL Cholesterol mgdL

# Finding the value of k
# For this example we use k  3 because patients can be divided into three simple groups Low Risk Medium Risk and High Risk

# Clusters k  3

#  Cluster 1  Low Risk Normal blood pressure normal glucose level and low LDL cholesterol

#  Cluster 2  Medium Risk Slightly high blood pressure increased glucose level and high LDL cholesterol

#  Cluster 3  High Risk High blood pressure very high glucose level and very high LDL cholesterol

import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

X = np.array([ [115,85,90], [118,88,95], [120,90,100], [112,82,85], [117,86,92], [119,89,98], [116,84,88], [121,91,102], [114,83,87], [118,87,94], [135,115,145], [138,120,150], [132,110,140], [140,125,155], [136,118,148], [134,112,142], [142,128,160], [137,116,146], [130,108,138], [139,122,152], [165,180,210], [170,190,220], [175,200,230], [160,175,205], [180,210,250], [168,185,215], [172,195,225], [178,205,240], [162,178,208], [185,220,260], [116,86,91], [119,90,97], [113,81,84], [122,92,103], [115,85,89], [120,88,96], [117,87,93], [111,80,82], [118,89,99], [121,90,101], [133,114,144], [141,126,158], [135,117,147], [138,121,151], [131,109,139], [143,130,162], [136,115,145], [140,123,154], [134,111,141], [139,119,149] ])

model = KMeans(n_clusters=3,random_state=42,n_init=3)

#train model 
model.fit(X)

#extract labels
labels = model.labels_

#print(label)
print("labels = ",labels)

# print centroids
print(model.cluster_centers_)

#data 
patients = [ "Aarav","Aditi","Rohan","Priya","Arjun", "Neha","Rahul","Sneha","Vikram","Pooja", "Karan","Ananya","Rajesh","Kavita","Amit", "Nisha","Suresh","Riya","Manish","Divya", "Akash","Simran","Nitin","Pallavi","Ravi", "Shreya","Vivek","Isha","Sanjay","Meera", "Harsh","Komal","Deepak","Swati","Yash", "Tanvi","Prakash","Anjali","Mohit","Payal", "Abhishek","Kajal","Rakesh","Mansi","Dhruv", "Sonal","Pankaj","Bhavna","Kunal","Radhika" ]

for patient,data,label in zip(patients,X,labels): 
    print(f"Name : {patient} data = {data} label = {label}")

#create chart
plt.scatter(labels,X[:,0],s=10)
plt.xticks(ticks=range(0,3),labels=range(0,3))
plt.ylabel("Systolic Blood Pressure")
plt.xlabel("Labels")
plt.show()


