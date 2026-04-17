#write a program to convert no of balls into hours and remaining ball in cricket

balls = int(input('enter balls'))

hours = balls // 60
balls = balls % 60

print('balls=',balls,'hours=',hours)
