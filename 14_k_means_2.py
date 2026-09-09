# KMeans algorithm 
# -------------------------------------------------------------------------------------------
#  1 ECommerce  Retail Customer Segmentation

# Features 3

#  Annual Spending 
#  Purchase Frequency ordersyear
#  Average Return Rate 

# Finding the value of k Elbow Method
# First standardize all three features using zscore Then run KMeans for k  1 to 8 and calculate WCSS From the elbow graph a clear bend can be seen at k  4

# Clusters k  4

#  Cluster 1  VIP Customers Spend a lot purchase frequently and have a low return rate

#  Cluster 2  HighRisk Customers Spend a lot but return many products

#  Cluster 3  Regular Budget Customers Spend less but purchase frequently and usually keep their products

#  Cluster 4  Occasional Customers Spend less and purchase only a few times

import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

X = np.array([[120000,45,2], [115000,42,3], [125000,48,2], [118000,44,4], [130000,50,2], [110000,40,25], [105000,38,28], [125000,45,30], [115000,42,27], [135000,50,32], [45000,35,5], [50000,38,4], [42000,32,6], [55000,40,5], [48000,36,7], [20000,8,3], [25000,10,4], [18000,6,2], [30000,12,5], [22000,9,3], [46000,36,5], [51000,39,4], [44000,34,6], [57000,40,5], [47000,35,7], [53000,38,4], [41000,31,5], [59000,42,6], [45000,33,4], [50000,37,5], [21000,9,3], [27000,10,4], [16000,6,2], [31000,12,5], [23000,8,3], [29000,11,4], [20000,7,2], [33000,13,5], [24000,8,3], [19000,7,4], [119000,44,3], [126000,48,2], [114000,41,4], [132000,51,2], [121000,46,3], [127000,49,2], [117000,43,3], [136000,53,2], [123000,47,4], [129000,50,2]])

model = KMeans(n_clusters=4,random_state=42,n_init=3)

#train model 
model.fit(X)

#extract labels
labels = model.labels_

#print(label)
print("labels = ",labels)

# print centeriods 
print(model.cluster_centers_)

#data 
customers = [ "Aarav","Aditi","Rohan","Priya","Arjun", "Neha","Rahul","Sneha","Vikram","Pooja", "Karan","Ananya","Rajesh","Kavita","Amit", "Nisha","Suresh","Riya","Manish","Divya", "Akash","Simran","Nitin","Pallavi","Ravi", "Shreya","Vivek","Isha","Sanjay","Meera", "Harsh","Komal","Deepak","Swati","Yash", "Tanvi","Prakash","Anjali","Mohit","Payal", "Abhishek","Kajal","Rakesh","Mansi","Dhruv", "Sonal","Pankaj","Bhavna","Kunal","Radhika" ]

for customer,data,label in zip(customers,X,labels):
    print(f"Name : {customer} data = {data} label = {label}")

#create chart
plt.scatter(labels,X[:,0],s=10)
plt.xticks(ticks=range(0,4),labels=range(0,4))
plt.ylabel("Annual Spending")
plt.xlabel("Labels")
plt.show()


