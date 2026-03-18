#write a program to convert inches into foot and remaining inches

inches = int(input('enter inches'))

foot = inches // 12
foot = foot % 12
print('inches=',inches,'foot=',foot)
