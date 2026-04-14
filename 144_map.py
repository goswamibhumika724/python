#write a program to generate cubes of all the numbers in list using map function 
numbers = [1,2,3,4,5,6,7,8,9,10]

cubes = map(lambda num: num * num * num,numbers)
print(list(cubes))