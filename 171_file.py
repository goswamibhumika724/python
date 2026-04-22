# write a program to display given file content on screen. also display how many line file has 
filename = input("Enter file name to read") 
mode = 'r' 

#file open
file = open(filename,mode) 
count = 0

#read text from file line by line 
for line in file:
    count = count + 1
    print(line.strip()) #remove new line character from both side of line
   
file.close() 
print('total lines',count)