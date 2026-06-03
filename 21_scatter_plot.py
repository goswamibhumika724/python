#Create a scatter chart displaying the score of RCB in each match since 2025.
import matplotlib.pyplot as plt

# RCB scores 
rcb_scores = [
    177, 196, 169, 221, 163, 175, 95, 230, 106, 190, 
    203, 250, 201, 240, 149, 175, 206, 77, 155, 203, 167, 194, 222, 200, 254, 161 
]

print(len(rcb_scores))

plt.figure(figsize=(18,8))
matches = list(range(1,len(rcb_scores)+1))
plt.scatter(matches,rcb_scores,s=60,c='red',alpha = 0.7,label='RCB scores')
plt.xlabel('match number')
plt.ylabel('rcb_scores')
plt.title('RCB scores from IPL 2025 and 2026 matches')
plt.legend()
plt.show()
