#write a program to findout mean value from all the argument passed in function 
def find_mean(*numbers):
    if len(numbers) == 0:
        return 0 
    return sum(numbers) / len(numbers)

#example usage
result = find_mean(10,20,30,40)
print('mean value is=',result)