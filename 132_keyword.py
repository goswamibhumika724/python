#write a program to create function return simple Interest using keyword argument concept 
def getsimpleinterest(amount,rate,year):
    simpleinterest = amount * rate * year / 100
    return simpleinterest

a = int(input('enter amount'))
r = int(input('enter rate'))
y = int(input('enter year'))

#call get simpleinterest
result = getsimpleinterest(amount=a,rate=r,year=y)
print(f'simpleinterest = {result}')




