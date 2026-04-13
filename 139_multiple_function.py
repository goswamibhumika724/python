#write a program to findout minimum & maximum from all the argument passed in function and return it 
def getmin_max(*numbers):
    max_val = numbers[0]
    min_val = numbers [0]
    for num in numbers:
         if num < min_val:
            min_val = num
         if num > max_val:
            max_val = num

    return min_val, max_val
       
         

result = getmin_max(10, 5, 8, 3, 99, 1, 200, 1000, 500, 200, 400, 570, 2000, 0)
print(result)
