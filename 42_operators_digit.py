#write a program to reverse 3 digit amount given by user
#input : number 567 output : number 765

amount = 567

amount = int(input("enter input"))

last = amount % 10 #7
print(last)

remaining = amount // 10 #76
print(remaining)

middle = remaining % 10 #6
print(middle)

first = remaining // 10 #5
print(first)


amount = (last * 100 + middle * 10 + first)
print(amount)

