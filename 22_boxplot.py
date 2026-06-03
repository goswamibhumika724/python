# Create a BoxPlot chart that display marks of 4 different division of school. each division is list that has marks of 50 students. 
#     A division marks range 40 to 50
#     B division marks range 51 to 65
#     C division marks range 66 to 80
#     D division marks range 81 to 90

import matplotlib.pyplot as plt

divisionA = [50, 41, 40, 44, 43, 43, 42, 41, 50, 48, 41, 49, 46, 40, 40, 41, 43, 43, 48, 49, 40, 48, 43, 50, 48, 46, 43, 47, 49, 44, 40, 42, 46, 45, 44, 42, 43, 45, 41, 41, 46, 41, 45, 45, 49, 44, 40, 47, 48, 41]

divisionB = [65, 57, 52, 59, 55, 64, 61, 60, 65, 64, 56, 60, 54, 62, 52, 51, 61, 54, 63, 55, 52, 64, 54, 64, 52, 57, 55, 58, 61, 64, 56, 53, 56, 56, 54, 61, 55, 62, 65, 61, 61, 52, 60, 61, 53, 59, 62, 54, 53, 58]

divisionC = [72, 70, 80, 76, 77, 74, 69, 76, 71, 79, 78, 78, 66, 69, 79, 66, 78, 71, 72, 70, 67, 69, 80, 75, 80, 77, 71, 69, 76, 73, 72, 80, 80, 76, 73, 68, 70, 68, 69, 77, 74, 74, 70, 77, 75, 72, 80, 75, 72, 71]

divisionD = [84, 83, 89, 88, 82, 81, 82, 83, 83, 87, 90, 82, 87, 87, 90, 88, 89, 85, 89, 81, 82, 89, 85, 86, 82, 85, 87, 83, 88, 81, 85, 89, 83, 89, 82, 85, 89, 90, 84, 83, 86, 83, 89, 89, 81, 90, 86, 88, 81, 82]
plt.figure(figsize=(8,6))
plt.boxplot([divisionA,divisionB,divisionC,divisionD],labels=['divisionA','divisionB','divisionC','divisionD'])
plt.xlabel('divisions')
plt.ylabel('student marks')
plt.title('School Marks Distribution by Division')
plt.show()