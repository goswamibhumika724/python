#write a program to calculate & display simple interest
#input is always string 
amount = input("enter amount")
rate = input("enter rate")
year = input("enter year")

#convert
amount = int(amount)
rate = float(rate)
year = int(year)

si = amount * rate * year /100
print("simple interest",si)

