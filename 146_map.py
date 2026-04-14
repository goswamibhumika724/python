#write a program to convert all the float  numbers into integer number of the list using map function 
numbers = [1.5, 2.8, 3.2, 4.9, 5.1]
integer = map(lambda num: int(num), numbers)
print(list(integer))
