#dictionary
book = {} #empty dictionary 
print(book)

#add key value pair
book['name'] = 'learning data science & ml'
book['chapter'] = [1,2,3,4,5] #chapter is list
book['topics'] = ('introduction to ml & ds','python','library','algorithms','models') #tuple in list
book['price'] = 1000

print(book)

book['topics'][0] = 'index' #error as topics is tuple
book['chapter'][0] = 10 #change is possible chapter is list
del book['price'] #scaler value
