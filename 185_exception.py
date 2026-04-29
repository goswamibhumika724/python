
from datetime import date 
# custom exception class
class InvalidDateError(Exception):
    pass

def acceptDate(msg):
        while True:
   
            try:
                print(msg)
                day = int(input("Enter day"))
                month = int(input("Enter month"))
                year = int(input("Enter year"))

                #valid date 
                birthday = date(year,month,day)
                return birthday
            
                
                
            except ValueError:
                print('Invalid date , enter correct date')
            
                 
birthday_1 = acceptDate("enter 1st brother's birth date (day, month and year as different input)")

birthday_2 = acceptDate("enter 2nd brother's birth date (day, month and year as different input)")

if birthday_1<birthday_2:
        print("1st brother is elder brother") 
elif birthday_1>birthday_2:
        print("2nd brother is elder brother")
else:
        print('both are same')
          
print("good bye")

