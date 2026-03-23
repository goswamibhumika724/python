#write a program to accept length and width of two different farm from user. and findout & display which farm is bigger 
#input length and width

length = int(input('enter length'))
width = int (input('enter width'))


area1 = length * width
#== != < > <= >=
if area1>0:
    print(f"length1 and width1{area1}")

length = int(input('enter length'))
width = int(input('enter width'))

area2 = length * width
if area2>0:
    print(f"length and width{area2}")

area = area1>area2
print(area)
