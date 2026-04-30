# create class tour to store below tour detail 
#         id,title,days,price,detail 
#         it also has one class variable which store tour operator name 
#         it should also have  constructor, display(display all instance variable ) method 
#         and display tour operator name outside class 
class tour:
    operator = 'shivay travels'
    def __init__(self,id,title,days,price,detail):
        self.id = id
        self.title = title
        self.days = days
        self.price = price
        self.detail = detail 
    def display(self):
        print('id',self.id)
        print('title',self.title)
        print('days',self.days)
        print('price',self.price)
        print('detail',self.detail)



            
print('operator (before)',tour.operator) 
tour.operator = 'gauri travels'
print('operator (after)',tour.operator)

# object creation
t1 = tour(1, "Jaipur Trip", 3, 15000, "HavaMahal,etc + Hotel + Food")

# display instance data
t1.display()





