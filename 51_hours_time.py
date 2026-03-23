# 1) write a program to convert 24 hours time into 12 hours format time and display it with AM PM message. 
# input : 15 hours 
# output  3 PM 

# input : 11 hours 
# output  11 AM 

# input : 25 hours 
# output  invalid input 

hours = int(input('enter hours'))

difference  = hours - 12
# == != < > <= >=
if difference>0:
    print(f"format time with{difference}pm")

difference = hours - 12
if difference>0:
    print(f"format time with{difference}am")

difference = hours - 12
if difference>0:
    print(f"invalid output{difference}")
    