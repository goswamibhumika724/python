#write a program to convert decimal number into octal number using recursion 
def printoctal(number):
    if number > 0:
        reminder = number % 8
        number = number // 8 
        printoctal(number)
        print(reminder,end='')

number = int(input("Enter number"))
print('octal:', end=' ')
printoctal(number)