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

# thislist = ["apple","banana","mango","orange"]
# x= thislist.count("apple")
# print(x)

# thislist = ["apple","banana","mango","orange"]
# thislist.clear()
# print(thislist)


# thislist = ["apple","banana","mango","orange"]
# thislist.append("carrot")
# thislist.sort()
# print(thislist)

# thislist = ["apple","banana","mango","orange"]
# newlist = list(thislist)
# print(newlist)


# thislist = ["apple","banana","mango","orange"]
# newlist = ["carrot","grapes"]
# thislist.extend(newlist)
# thislist.sort()
# print(thislist)

# thislist = ["apple","banana","mango","orange"]
# newlist = ["carrot","grapes"]
# thislist.extend(newlist)
# thislist.sort()
# print(thislist)
# print(thislist.index("mango"))

# thislist = ["apple","banana","mango","orange"]
# thislist.insert(1,"apple")
# print(thislist)

# thislist = ["apple","banana","mango","orange"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple","banana","mango","orange"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple","banana","mango","orange"]
# thislist.reverse()
# print(thislist)

# thislist = ["apple","banana","mango","orange"]
# thislist.sort(reverse=True)
# print(thislist)

# thislist = ["apple","banana","mango","orange"]
# thislist.sort()
# print(thislist)

'''Basic:

Create a list:

Create a list called fruits containing the following items: "apple", "banana", "cherry", "grape".
Access elements:

Print the second element of the fruits list.
Print the last element of the fruits list.
Modify elements:

Change the third element of the fruits list to "orange".
Add "kiwi" to the end of the fruits list.
List length:

Find the length of the fruits list.
Check for membership:

Check if "apple" is present in the fruits list.
Check if "pineapple" is present in the fruits list.
Intermediate:

Sort a list:

Create a list called numbers containing the following numbers: 5, 2, 8, 1, 9.
Sort the numbers list in ascending order.
Sort the numbers list in descending order.
Reverse a list:

Reverse the order of elements in the numbers list.
Remove duplicates:

Create a list called colors containing the following colors: "red", "blue", "green", "red", "yellow", "blue".
Remove duplicate colors from the colors list.
Concatenate lists:

Create two lists: list1 with elements [1, 2, 3] and list2 with elements [4, 5, 6].
Combine the elements of list1 and list2 into a new list called combined_list.
Find the maximum and minimum:

Find the maximum and minimum values in the numbers list.
Advanced:

Nested lists:
Create a nested list called matrix representing a 3x3 matrix:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Access the element at row 2, column 1 (which should be 8).
Print all the elements of the matrix in a formatted way.
List comprehension:
Create a new list called squares containing the squares of numbers from 1 to 10 using list comprehension.
Filtering lists:
Create a list called numbers containing the following numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.
Create a new list called even_numbers containing only the even numbers from numbers using list comprehension.
Mapping lists:
Create a list called temperatures containing the following temperatures in Celsius: 25, 28, 30, 22.
Convert each temperature to Fahrenheit using list comprehension and store the results in a new list called fahrenheit_temperatures.
Custom sorting:
Create a list called students containing dictionaries representing student information:
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 19},
    {"name": "Charlie", "age": 21}
]
Sort the students list by age in ascending order.
Bonus:

Write a function to find the second largest element in a list.
Write a function to remove all occurrences of a specific element from a list.
Write a function to check if a list is sorted in ascending order.
Remember to use the appropriate Python list methods and techniques to solve these problems. Good luck!'''