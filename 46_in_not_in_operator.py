countries = "india, china, japan, south korea, north korea, indonesia, thailand, vietnam, malaysia, singapore, philippines, bangladesh, pakistan, sri lanka, nepal, bhutan, myanmar, saudi arabia, united arab emirates, turkey"


word = "india"
result = word in countries
print(result)

result = word not in countries
print(result)

word = "cyprus"
result = word in countries
print(result)

result = word not in countries
print(result)

fruits = [
    "apple",
    "banana",
    "mango",
    "orange",
    "pineapple",
    "strawberry",
    "grapes",
    "watermelon",
    "papaya",
    "guava"
]

item = "banana"
print(item in fruits)
print(item not in fruits)

places = (
    "varanasi",
    "haridwar",
    "rishikesh",
    "kedarnath",
    "badrinath",
    "tirupati",
    "jagannath puri",
    "dwarka",
    "ayodhya",
    "mathura"
)

location = "mathura"
print(location in places)
print(location not in places)
