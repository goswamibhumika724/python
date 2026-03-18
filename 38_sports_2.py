#create a python program to create 2 set.
# 1 set has list of sports include in olympic 2016
# 2 set has list of sports include in olympic 2022

#sports_2016 



olympic_2016 = [
    "Archery",
    "Athletics",
    "Badminton",
    "Basketball",
    "Boxing",
    "Canoeing",
    "Cycling",
    "Diving",
    "Equestrian",
    "Fencing",
    "Field Hockey",
    "Football",
    "Golf",
    "Gymnastics",
    "Handball",
    "Judo",
    "Modern Pentathlon",
    "Rowing",
    "Rugby Sevens",
    "Sailing",
    "Shooting",
    "Swimming",
    "Synchronized Swimming",
    "Table Tennis",
    "Taekwondo",
    "Tennis",
    "Triathlon",
    "Volleyball",
    "Water Polo",
    "Weightlifting",
    "Wrestling"]
print(olympic_2016)

    


olympic_2022 = [
    "Alpine Skiing",
    "Biathlon",
    "Bobsleigh",
    "Cross-Country Skiing",
    "Curling",
    "Figure Skating",
    "Freestyle Skiing",
    "Ice Hockey",
    "Luge",
    "Nordic Combined",
    "Short Track Speed Skating",
    "Skeleton",
    "Ski Jumping",
    "Snowboarding",
    "Speed Skating"
]
print(olympic_2022)

#findout unique sports in both set & display it
unique_olympic_2016 = set(olympic_2016)
print(unique_olympic_2016)

unique_olympic_2022 = set(olympic_2022)
print(unique_olympic_2022)

#findout common sports in both set & display it
print(unique_olympic_2016.intersection(olympic_2016))
print(unique_olympic_2022.intersection(olympic_2022))

#findout sports in olympic 2022 but not in 2016 & display it
print(unique_olympic_2016.difference(olympic_2016))
print(unique_olympic_2022.difference(olympic_2022))

