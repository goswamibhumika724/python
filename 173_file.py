# write a program to count words in given file.
filename = input("Enter file name to read") 
mode = 'r' 

#file open
file = open(filename,mode) 
count = 0

#read text from file line by line 
for words in file:
    count = count + 1
    print(words.strip()) #remove new line character from both side of line
   
file.close() 
print('total words',count)