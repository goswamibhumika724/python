filename = input("Enter file name to read") #states.txt
mode = 'r'
try:
    file = open(filename,'r') 
    content = file.read()
    print(content)
    file.close() 

except FileNotFoundError:
    print('file not found, cheak file name')
    