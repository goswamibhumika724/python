# Error Bar Chart

# Create an error bar chart showing the scores of all IPL teams in the 2026 season.

import matplotlib.pyplot as plt

# 1. Prepare Data for IPL 2026 Teams
# Teams are sorted by their average match score in descending order
teams = [
    'Sunrisers Hyderabad', 'Royal Challengers Bengaluru', 'Gujarat Titans', 
    'Rajasthan Royals', 'Punjab Kings', 'Kolkata Knight Riders', 
    'Delhi Capitals', 'Chennai Super Kings', 'Mumbai Indians', 'Lucknow Super Giants'
]

# Average runs scored per match in the 2026 season
average = [192.5, 188.2, 185.6, 182.1, 178.4, 176.9, 174.2, 171.5, 168.0, 165.3]

# Match-to-match performance variance (Standard Error / Deviation)
errors = [15.4, 14.2, 16.1, 13.8, 12.5, 14.0, 15.1, 13.2, 16.5, 14.8]

plt.errorbar(teams,average,errors,color='blue',capsize=10,fmt='o')
plt.title("teams performance in IPL along with errors")
plt.xlabel("teams")
plt.xticks(teams,rotation=45)
plt.ylabel("average")
plt.grid()
plt.tight_layout()
plt.show()