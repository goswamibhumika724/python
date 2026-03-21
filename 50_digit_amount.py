#write a program to display 3 digit amount into words

amount = 789
amount = int(input('enter 3 digit amount'))
words = ['zero','one','two','three','four','five','six','seven','eight','nine']

last = amount % 10 #nine
remaining = amount // 10 #seven eight
middle = remaining % 10 #eight
first = remaining // 10 #seven

print(first,middle,last)
print(words[first],words[middle],words[last])


