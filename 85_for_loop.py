#display all negative values from list and also count it 
numbers =numbers = [-1, 2, -3, -4, -5, -6, 7 -8, -9, 10,
           -11, 12, -15, -17, -22, -23, 24, -25]
count = 1
for item in numbers:
    #print(item, end= ' ')
    reminder = item // 2 
    if reminder < 1:
        print(item, end= ' ')
        count+=1 
print('no of nagative values =',count)        