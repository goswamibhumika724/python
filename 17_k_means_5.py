# 4 Real Estate Housing Area Segmentation

# Features 3

#  Price per Square Foot ft
#  Distance from Transit Hub km
#  School Rating 110

# Finding the value of k
# For this example we choose k  4 to divide housing areas into four groups based on price transportation and school quality

# Clusters k  4

#  Cluster 1  Premium Areas High property prices and very close to public transport

#  Cluster 2  Family Areas Higher property prices but farther from transport with very good schools

#  Cluster 3  Average Areas Medium property prices reasonably close to transport and average schools

#  Cluster 4  Budget Areas Low property prices far from transport and lower school ratings

import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

X = np.array([ [8500,0.5,9], [9000,0.8,9], [8200,0.6,8], [9500,0.4,10], [8800,0.7,9], [9200,0.9,8], [8700,0.5,9], [9800,0.3,10], [9100,0.6,9], [8900,0.8,8], [7000,5.0,10], [7500,5.5,9], [6800,4.8,10], [7800,6.0,9], [7200,5.2,10], [8000,5.8,9], [7400,4.5,10], [7600,5.0,9], [7100,6.2,10], [7900,5.6,9], [4500,2.5,6], [4800,3.0,7], [4200,2.8,6], [5000,3.5,7], [4700,2.2,6], [5200,3.2,7], [4400,2.7,6], [4900,3.1,7], [4600,2.4,6], [5100,3.4,7], [2200,8.0,4], [2500,9.0,3], [2000,7.5,4], [2800,10.0,5], [2300,8.5,3], [2600,9.5,4], [2100,7.8,3], [2900,10.5,5], [2400,8.2,4], [2700,9.2,3], [8300,0.9,8], [9400,0.5,9], [8600,0.7,9], [9700,0.4,10], [8900,0.6,8], [9300,0.8,9], [8500,0.5,9], [9900,0.3,10], [9000,0.7,8], [8700,0.9,9] ])

model = KMeans(n_clusters=4,random_state=42,n_init=5)

#train model 
model.fit(X)

#extract labels
labels = model.labels_

#print(label)
print("labels = ",labels)

# print centroids
print(model.cluster_centers_)

#data 
areas = [ "Aarav","Aditi","Rohan","Priya","Arjun", "Neha","Rahul","Sneha","Vikram","Pooja", "Karan","Ananya","Rajesh","Kavita","Amit", "Nisha","Suresh","Riya","Manish","Divya", "Akash","Simran","Nitin","Pallavi","Ravi", "Shreya","Vivek","Isha","Sanjay","Meera", "Harsh","Komal","Deepak","Swati","Yash", "Tanvi","Prakash","Anjali","Mohit","Payal", "Abhishek","Kajal","Rakesh","Mansi","Dhruv", "Sonal","Pankaj","Bhavna","Kunal","Radhika" ]
for area,data,label in zip(areas,X,labels): 
    print(f"Name : {area} data = {data} label = {label}")

#create chart
plt.scatter(labels,X[:,0],s=10)
plt.xticks(ticks=range(0,4),labels=range(0,4))
plt.ylabel("price per sq foot")
plt.xlabel("Labels")
plt.show()

