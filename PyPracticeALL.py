# import sys
# print(sys.version)

# unpacking

# grocery = ["Sugar","oil","Soap"]
# x, y, z = grocery
# print(x)
# print(y)
# print(z)

# output variable

# x = "I"
# y = "Love"
# z = "Pyhon"
# print(x,y,z)

# x = "I"
# y = "Love"
# z = "Pyhon"
# print(x+y+z)

# randon number

# import random

# print(random.randrange(0, 11))#this print any random number between 0 to 10

# multiline string

# x = """This is a multiline string
# This is a multiline string
# This is a multiline string
# This is a multiline string
# This is a multiline string"""
# print(x)

                           #or
# y = '''This is a multiline string
# This is a multiline string
# This is a multiline string
# This is a multiline string
# This is a multiline string'''
# print(y)

# strings are arrays

# x = "Hello World!"
# print(x[1])

# looping through string

# for x in "python":
#     print(x)

# indentation is important

# string leght

# x = "I Love Python!"
# print(len(x))

# check if a certain phrase or character is present in a string or not 

# x = "i love the way i live"
# print("live" in x)

# x = "i love the way i live"
# if "live" in x:
#     print("YES, 'live' is present")

# x = "i love the way i live"
# if "life" not in x:
#     print("NO, 'life' is not present")

# negative indexing

# a = "love python1"
# print(a[-7:-1])

# modify string

# a = "Hello My name is Nishant"
# print(a.upper())

# a = "  Hello My name is Nishant  "
# print(a.strip())

# a = "Hello My name is Nishant"
# print(a.replace("My", "he's"))

# a = "Hello, My name, is Nishant"
# print(a.split(","))

# string concatenation

# a = "hello"
# b = "world"
# print(a+ " " + b)

# price = 250
# txt = f"the price is {price:.2f} in dollers"
# print(txt)

# txt = f"the multiplication of 5 and 4 is {5*4}"
# print(txt)

# age = 19
# txt = f"My name is Nishant, I am {age}"
# print(txt)

# txt = "hello we are \"engineers\"\\ We are innovative"
# print(txt)

# a = 25
# print(isinstance(a, str))

# listttttt

# thislist = ["apple","banana","mango","orange"]
# print(len(thislist))

# thislist = ["apple","banana","mango","orange"]
# print(type(thislist))

# thislist = list(("apple","mango","banana"))
# print(thislist)

# thislist = ["apple","banana","mango","orange"]
# print(thislist[-3:-1])

# thislist = ["apple","banana","mango","orange"]
# if "pineapple" in thislist:
#     print("The fruit is present")
# else:
#     print("Fruit is absent")

# thislist = ["apple","banana","mango","orange"]
# thislist[2] ="unknown"
# print(thislist)

# thislist = ["apple","banana","mango","orange"]
# thislist.append("Fruit")
# print(thislist)

# thislist = ["apple","banana","mango","orange"]
# favfruit = ["grapes","pineapple"]
# newlist = thislist
# newlist.extend(favfruit)
# print(newlist)

# thislist = ["apple","banana","mango","orange"]
# thislist.remove("mango")
# print(thislist)


# thislist = ["apple","banana","mango","orange"]
# thislist.pop(2)
# print(thislist)


# thislist = ["apple","banana","mango","orange"]
# thislist.pop()
# print(thislist)


# thislist = ["apple","banana","mango","orange"]
# del thislist[2]
# print(thislist)

# thislist = ["apple","banana","mango","orange"]
# thislist.clear()
# print(thislist)

# thislist = ["apple","banana","mango","orange"]
# del thislist[1]
# print(thislist)

# thislist = ["apple","banana","mango","orange"]
# for i in thislist:
#     print(i)

# thislist = ["apple","banana","mango","orange"]
# for i in range(len(thislist)):
#     print(thislist[i])

# thislist = ["apple","banana","mango","orange"]
# i=0
# while i < len(thislist):
#     print(thislist[i])
#     i +=1

# thislist = ["apple","banana","mango","orange"]
# [print(i) for i in thislist]

