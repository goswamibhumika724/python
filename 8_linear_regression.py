# linear regression
# ------------------------------------------------------
# There are 2 input features in each exercise.

# Exercise 1: Predicting Student Exam ScoresScenario: An education researcher wants to analyze how student study habits and class engagement impact final exam performance.Input Features ($X$):$X_1$: Hours studied per week$X_2$: Attendance rate (percentage)Target Variable ($Y$): Final exam score (out of 100)Practice Goal: Train a model to find out whether study hours or attendance has a stronger weight on the final score.
import numpy as np 
from sklearn.linear_model import LinearRegression

student_habits = np.array([
    [18.5, 92.4], [10.2, 78.1], [24.1, 95.0], [6.5, 62.3], [14.8, 85.6],
    [8.0, 71.2], [22.4, 91.8], [12.1, 80.5], [5.2, 58.9], [19.7, 88.3],
    [16.3, 84.0], [7.4, 69.5], [26.0, 98.2], [11.5, 75.6], [13.9, 82.1],
    [9.1, 74.3], [21.0, 90.0], [4.8, 55.4], [17.6, 86.7], [15.2, 83.5],
    [23.5, 94.1], [8.7, 70.8], [12.8, 79.4], [6.0, 64.0], [20.3, 89.2],
    [10.9, 76.8], [25.4, 96.5], [14.1, 81.9], [7.8, 68.0], [18.0, 87.4],
    [11.2, 77.0], [5.9, 61.5], [22.8, 93.0], [16.8, 85.2], [9.5, 72.6],
    [13.4, 80.9], [24.8, 97.1], [8.3, 67.4], [19.1, 88.9], [6.8, 63.8],
    [15.7, 84.6], [10.5, 75.0], [21.9, 92.7], [4.2, 52.1], [17.2, 86.0],
    [12.4, 78.8], [27.1, 99.0], [9.8, 73.1], [14.5, 83.0], [7.1, 66.2]
])

exam_scores = np.array([
    84.2, 66.5, 93.8, 52.1, 75.4,
    60.9, 89.6, 70.3, 48.7, 83.1,
    77.8, 58.4, 96.7, 67.9, 73.2,
    63.4, 87.5, 45.2, 80.6, 76.1,
    91.3, 61.8, 71.0, 53.9, 85.0,
    67.1, 95.2, 74.0, 59.5, 81.9,
    68.3, 51.4, 90.1, 78.6, 64.2,
    72.5, 94.4, 60.1, 83.7, 54.8,
    76.9, 66.0, 88.3, 42.6, 79.8,
    70.8, 98.1, 64.7, 74.9, 57.3
])

#create model 
model = LinearRegression()

#model train 
model.fit(student_habits,exam_scores)

#prediction
student = np.array([[2.0,66.3]])
print("predicted score for student with 2 study hours and 66% attendance is" ,model.predict(student))

student_2 = np.array([[17.0,80.3]])
print("predicted score for student_2 with 17 study hours and 80% attendance is" ,model.predict(student_2))

