#write a program to convert all the negative numbers into positive number in list using map function 
numbers = [10, -5, 7, -2, 0, 3, -8]
positive_nagative = map(lambda num: -num if num < 0 else num, numbers)
print(list(positive_nagative))

