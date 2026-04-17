#write a program to convert given grams into kilograms and remaining grams
grams = int(input('enter gram'))

kilograms = grams // 1000
grams = grams % 1000

print('grams=',grams,'kilograms=',kilograms)
