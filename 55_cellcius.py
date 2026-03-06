#write a program to convert & display ferenhit into cellcius
#input
ferenhit = input("enter ferenhit")
#convert
ferenhit = float(ferenhit)
cellcius = (ferenhit - 32) /1.8
cellcius = round(cellcius,2)
print("cellcius=",cellcius)
