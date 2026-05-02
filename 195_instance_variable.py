# create class product to store below product Detail
#         id,name,price,weight 
#     it should have constructor, display(display all instance variable ) method and pricePerGram() method 
class product:
    shop = 'Shiv Book Stall'

    #constructor
    def __init__(self,id,name,price,weight):
        self.id = id
        self.name = name
        self.price = price
        self.weight = weight
        print("constructor method is called.")
    def display(self):
        print('id',self.id)
        print('name',self.name)
        print('price',self.price)
        print('weight',self.weight)
        print('shop',product.shop)

    def pricepergram(self):
          if self.weight != 0:
            return self.price / self.weight
          else:
            return 0

id =  int(input('enter product id'))    
name = input('enter product name')
price = int(input('enter product price'))
weight = int(input('enter product weight'))

p1 = product(id,name,price,weight)
p1.display()

ppg = p1.pricepergram()
print(f"pricepergram = {ppg}")


