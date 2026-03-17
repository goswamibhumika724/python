#write dictionary to store your college details like name,trust,principal,establishment year,address,city,courses etc
college = {'name':'nandkuvarba mahila college','trust':'None','principal':'samkit shah','establishment year':1982,'address':'devraj nagar','city':'bhavnagar','courses':['b.a','b.com','fashion design']}

print(college)

#update city using update method
college['city'] = 'surat'
print(college)

#add state
college['state'] = 'gujarat'
print(college)
#display all keys
print(college.keys())

#display all values
print(college.values())
#remove state
college.pop('state')
print(college)
#remove last itempair
college.popitem()
print(college)

college2 = college.copy()
print(college2)
college.clear()
print(college2)




