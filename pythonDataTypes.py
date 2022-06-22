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

# import string

# # print("Enter String: ")
# # String1 = string(input("String is : "))
# print("Initial String is : ")
# String1 = "GeeksForGeeks"
# print(String1)

# # Printing First character
# print("\nFirst character of String is: ")
# print(String1[0])

# # Printing Last character
# print("\nLast character of String is: ")
# print(String1[-1])

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#List
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# List = []
# print("Printing empty list")
# print(List)

# list1 = ['DeepakRaj']
# list2 = ['Deepak raj']

# print("printing list with data")
# #print(list)
# print(list1)
# print(list2)

# list3 = ["Deepak",19,"Raj",987654321]
# print(list3)
# print(list3[2])
# print(list3[-4])

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Tuple
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Tuple1 = ()
# print("Creating empty tuple")
# print(Tuple1)

# list1 = [1,2,3,4,5,6,7,8,9,10]
# print(tuple(list1))

# Tuple1 = [9,7,6,5,4,3,2,1,0]
# Tuple2 = ("Deepak", "Raj")
# Tuple3 = (Tuple1, Tuple2)
# print(Tuple3)



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Boolean
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# print(type(True))
# print(type(False))

# print(type(true))

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#sets
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# set1 = set()
# print(set1)

# set2 = set("Deepak Raj")
# print(set2)

# set3 = set(["A","B","C","D","E","F"])
# print(set3)


# Creating a set
# set5 = set(["Deepak", "Raj", "Kantilal"])
# print("\nInitial set")
# print(set5)

# # Accessing element using
# # for loop
# print("\nElements of set: ")
# for i in set5:
#     print(i, end =" ")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Dictionary
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Dict = {}
# print(Dict)

# Dict1 = {1:'Deepak',2:"Raj",3:'Kantilal'}
# print(Dict1)

# Dict2 = {'Name': 1, 'Age':21, "MobileNo": 9876543210}
# print(Dict2)


# accessing a element from a Dictionary

# Creating a Dictionary
Dict = {2: 'Raj', 'Age': '22', 3: 'Deepak'}

# accessing a element using key
print("Accessing a element using key:")
print(Dict['Age'])

# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(3))
