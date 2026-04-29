
filename = input("Enter file name to read") #states.txt
mode = 'r' 

try:
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print('file is not found,cheak the file name')


 

