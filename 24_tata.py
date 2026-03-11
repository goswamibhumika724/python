#create empty list cars
cars = [] #empty list
print(cars)

#add new car
cars.append('maruti')
cars.append('tata')
cars.append('mahindra')
print(cars)

#add new car at 0 position
cars.insert(0,'bmw')
#add another car at 1st position
cars.insert(1,'mercedes')
print(cars)

scooters = ['activa','pept','access']
#merge cars into scooters
cars.extend(scooters)
print(cars)

#remove car from 0 position
cars.pop(0)
print(cars)

#empty list scooters
scooters.clear()
print(scooters)




