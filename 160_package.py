#Create Package India which has 4 sub package 
import india.north.language as no 
import india.south.language as so
import india.east.language as  es
import india.west.language as we 

#function calling of package 
print(no.getlanguage())
print(so.getlanguage())
print(es.getlanguage())
print(we.getlanguage())


result = no.islanguageexist("Hindi")
print(f"is language existing in north_india ",result)

result = so.islanguageexist("Tamil")
print(f"is language existing in south_india ",result)

result = es.islanguageexist("Marwari")
print(f"is language existing in east_india ",result)

result = we.islanguageexist("Bhojpuri")
print(f"is language existing in west_india ",result)