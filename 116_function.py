#write a program that return simple interest of given amount rate year
def getsimpleinterest(amount,rate,year):
    simpleinterest = amount * rate * year / 100
    return simpleinterest

amount = int(input('enter amount'))
rate = int(input('enter rate'))
year = int(input('enter year'))

#call get simpleinterest
result = getsimpleinterest(amount,rate,year)
print('simpleinterest=',result)





