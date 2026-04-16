#write a program to decide which is cheaper approach to go from ahmedabad to delhi. by car or by train. consider person has his own petrol car  and he prefer to travel by 1st class train 
#take input car 
#input train

train = int(input('enter price'))   
average = int(input('enter average'))
petrol = int(input('enter petrol'))
kilometer = int(input('enter kilometer'))

car = average * petrol 
print(car)
if car>0:
    print(f"price of car{car}")
if train>0:
    print(f"price of train{train}")    

