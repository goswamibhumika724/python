# logistic regression 
# ----------------------------------------------------------------
# There are 2 input features in each exercise.

# Exercise 1: FinanceDevelop a logistic regression example that will predict whether a loan applicant will Default ($y=1$) or Not Default ($y=0$) based on two input features: Debt-to-Income ratio ($x_1$) and Credit Score ($x_2$).

import numpy as np
from sklearn.linear_model import LogisticRegression

# Input features: [Debt-to-Income ratio (x1), Credit Score (x2)] (100 rows)
X = np.array([
    [0.15, 750], [0.20, 720], [0.45, 580], [0.10, 800], [0.50, 530],
    [0.30, 650], [0.55, 600], [0.25, 700], [0.40, 610], [0.18, 760],
    [0.12, 790], [0.48, 550], [0.22, 710], [0.35, 640], [0.60, 520],
    [0.14, 770], [0.28, 680], [0.42, 590], [0.16, 740], [0.52, 540],
    [0.11, 810], [0.33, 630], [0.58, 510], [0.21, 730], [0.38, 620],
    [0.19, 755], [0.46, 570], [0.24, 705], [0.32, 645], [0.53, 535],
    [0.13, 785], [0.27, 685], [0.41, 595], [0.17, 745], [0.51, 545],
    [0.15, 765], [0.29, 675], [0.44, 585], [0.20, 725], [0.49, 555],
    [0.10, 820], [0.31, 655], [0.56, 515], [0.23, 715], [0.37, 625],
    [0.18, 750], [0.47, 565], [0.26, 695], [0.34, 635], [0.54, 525],
    [0.16, 735], [0.22, 700], [0.40, 600], [0.12, 800], [0.55, 500],
    [0.30, 660], [0.50, 550], [0.25, 720], [0.38, 615], [0.15, 775],
    [0.11, 830], [0.45, 575], [0.21, 710], [0.36, 630], [0.59, 510],
    [0.14, 780], [0.28, 670], [0.43, 590], [0.17, 735], [0.52, 530],
    [0.13, 795], [0.29, 665], [0.41, 605], [0.19, 745], [0.48, 560],
    [0.10, 840], [0.32, 640], [0.57, 520], [0.24, 700], [0.39, 610],
    [0.18, 760], [0.46, 580], [0.26, 690], [0.33, 635], [0.53, 535],
    [0.15, 770], [0.27, 680], [0.42, 595], [0.20, 730], [0.51, 540],
    [0.12, 805], [0.30, 650], [0.54, 525], [0.23, 715], [0.37, 625],
    [0.16, 755], [0.44, 585], [0.25, 705], [0.35, 640], [0.50, 545]
])

# Output labels: Default (1) or Not Default (0) (100 rows corresponding to X)
y = np.array([
    0, 0, 1, 0, 1, 0, 1, 0, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1,
    0, 0, 1, 0, 0, 0, 1, 0, 0, 1,
    0, 0, 1, 0, 1, 0, 0, 1, 0, 1,
    0, 0, 1, 0, 0, 0, 1, 0, 0, 1,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1,
    0, 0, 1, 0, 1, 0, 0, 1, 0, 0,
    0, 1, 1, 0, 1, 0, 0, 1, 0, 1,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 1
])

#create model
model = LogisticRegression()
print("model training started.....")

#model train
model.fit(X,y) # input, label (output)

print("model training complete.....")


# Prediction for a new loan applicant [Debt-to-Income ratio, Credit Score]
applicant_1 = np.array([[0.44,540]])
prediction = model.predict(applicant_1)

print("Loan default prediction applicant_1 (0: No Default, 1: Default) = ", prediction)

# Probability prediction
print("Loan default prediction probability = ", model.predict_proba(applicant_1))

applicant_2 = np.array([[0.16,701]])
prediction = model.predict(applicant_2)

print("Loan default prediction applicant_2 (0: No Default, 1: Default) = ", prediction)

# Probability prediction
print("Loan default prediction probability = ", model.predict_proba(applicant_2))

# Model accuracy
print("Model accuracy = ", model.score(X, y))
 