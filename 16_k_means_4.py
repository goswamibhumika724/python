#  3 Telecommunications Mobile User Segmentation

# Features 4

#  Monthly Data Usage GB
#  Domestic Call Minutes
#  International SMS Count
#  OffPeak Data Usage Ratio

# Finding the value of k Elbow Method
# Run KMeans for different values of k and calculate inertia The elbow graph shows a clear bend at k  3

# Clusters k  3

#  Cluster 1  Heavy Data Users Use a large amount of mobile data but make fewer calls

#  Cluster 2  Calling Users Use less data but make many phone calls and send many SMS messages

#  Cluster 3  Night Users Use a moderate amount of data especially during offpeak hours

import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

#create dataset 
X = np.array([ [25,80,20,0.25], [30,75,18,0.20], [28,90,22,0.30], [35,70,15,0.22], [32,85,20,0.28], [27,78,17,0.24], [40,65,14,0.18], [38,72,16,0.21], [33,88,19,0.27], [29,82,21,0.26], [5,600,120,0.15], [7,650,140,0.18], [6,580,110,0.16], [8,700,150,0.20], [9,620,135,0.17], [6,680,125,0.19], [10,750,160,0.21], [7,610,130,0.16], [8,670,145,0.18], [5,590,115,0.15], [18,200,40,0.75], [20,220,45,0.80], [16,180,35,0.72], [22,240,50,0.85], [19,210,42,0.78], [24,250,55,0.88], [17,195,38,0.74], [21,230,48,0.82], [23,245,52,0.86], [18,205,40,0.76], [26,85,19,0.23], [31,78,17,0.21], [29,92,23,0.29], [36,73,16,0.24], [34,87,21,0.27], [28,80,18,0.25], [39,68,13,0.19], [37,76,15,0.22], [32,90,20,0.28], [30,84,22,0.26], [6,630,125,0.17], [8,690,145,0.19], [7,570,108,0.15], [9,720,155,0.21], [5,600,118,0.16], [10,740,165,0.20], [6,660,135,0.18], [8,710,150,0.22], [7,640,128,0.17], [9,680,142,0.19] ])

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
users = [ "Aarav","Aditi","Rohan","Priya","Arjun", "Neha","Rahul","Sneha","Vikram","Pooja", "Karan","Ananya","Rajesh","Kavita","Amit", "Nisha","Suresh","Riya","Manish","Divya", "Akash","Simran","Nitin","Pallavi","Ravi", "Shreya","Vivek","Isha","Sanjay","Meera", "Harsh","Komal","Deepak","Swati","Yash", "Tanvi","Prakash","Anjali","Mohit","Payal", "Abhishek","Kajal","Rakesh","Mansi","Dhruv", "Sonal","Pankaj","Bhavna","Kunal","Radhika" ]

for user,data,label in zip(users,X,labels): 
    print(f"Name : {user} data = {data} label = {label}")

#create chart
plt.scatter(labels,X[:,0],s=10)
plt.xticks(ticks=range(0,3),labels=range(0,3))
plt.ylabel("Monthly Data Usage GB")
plt.xlabel("Labels")
plt.show()

