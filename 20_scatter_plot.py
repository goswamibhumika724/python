#Create a scatter chart displaying the age of patient at the time of death in covid 19.

import matplotlib.pyplot as plt

covid_age_death = [
    84, 72, 65, 91, 58, 80, 77, 69, 83, 74, 
    61, 88, 79, 71, 66, 53, 82, 75, 93, 70, 
    63, 78, 85, 68, 81, 76, 59, 86, 73, 67, 
    45, 87, 89, 62, 80, 95, 74, 57, 72, 84
]


print(len(covid_age_death))

plt.figure(figsize=(18,8))
patient = list(range(1,len(covid_age_death)+1))
plt.scatter(patient,covid_age_death,s=25,c='purple',label='india covid19 death')
plt.xlabel('patient number')
plt.ylabel('age of death')
plt.title('india age of death in covid19')
plt.legend()
plt.show()
