#write a program to filter all the players who have score more then 50 runs in match. use list and filter function 
cricketers = [
    ("Virat Kohli", 65),
    ("Rohit Sharma", 45),
    ("Shubman Gill", 78),
    ("Rishabh Pant", 30),
    ("KL Rahul", 55),
    ("Hardik Pandya", 40),
    ("MS Dhoni", 70)
]

print(cricketers)

score = filter(lambda player: player[1] > 50,cricketers ) 
print(list(score))