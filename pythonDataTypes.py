# #Data types in python
# # Python Program for
# # Creation of String

# # Creating a String
# # with single Quotes
# String1 = 'Welcome to the Geeks World'
# print("String with the use of Single Quotes: ")
# print(String1)

# # Creating a String
# # with double Quotes
# String1 = "I'm a Geek"
# print("\nString with the use of Double Quotes: ")
# print(String1)
# print(type(String1))

# # Creating a String
# # with triple Quotes
# String1 = '''I'm a Geek and I live in a world of "Geeks"'''
# print("\nString with the use of Triple Quotes: ")
# print(String1)
# print(type(String1))

# # Creating String with triple
# # Quotes allows multiple lines
# String1 = '''Geeks
# For
# Life'''
# print("\nCreating a multiline String: ")
# print(String1)


# # Accessing elements of String

# Python Program to Access
# characters of String

import string

# print("Enter String: ")
# String1 = string(input("String is : "))
print("Initial String is : ")
String1 = "GeeksForGeeks"
print(String1)

# Printing First character
print("\nFirst character of String is: ")
print(String1[0])

# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])