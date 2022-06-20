# Introduction to python
  # Hello message
  # print("hello")

  # Variables {
  # myNum = 10
  # print(myNum)

  # myNum1 = 10.40
  # print(myNum1)

  # }

  # Creating list
  # nums = []

  # nums.append(5)
  # nums.append("Hello")
  # nums.append(10.5)
  # print(nums)

  # # Python program to illustrate
  # # functions
  # def hello():
  #     print("hello")
  #     print("hello again")
  # hello()

  # # calling function
   # hello()

   # Python program to illustrate
  # function with main
#   from unittest import result

#    def getInteger():
#         result = int(input("Enter integer: "))
#         # result = 10;
#         return result

#     def Main():
#         print("Started")

#         # calling the getInteger function and
#         # storing its returned value in the output variable
#         output = getInteger()
#         print(output)

#     # now we are required to tell Python
#     # for 'Main' function existence
#     if __name__ == "__main__":
#         Main()

#====================================================================
# Basics of Python
#if else condition
from unittest import result

# def getInteger():
# a = input("Enter value of A: ")
# b = input("Enter  value of B: ")

a = int(input("Enter Value of A: "))
b = int(input("Enter Value of B: "))
    # return a,b

    # if b > a == 0:
    #     print("B is greater")
    # else: 
    #     print("A is greater")
    
if b % a == 0 :
    print ("b is divisible by a")
elif b + 1 == 10:
    print ("Increment in b produces 10")
else:
    print ("You are in else statement")


# def Main():
#     print("Starting program")
#     output  = getInteger()
#     print("Value of A & B")
#     print(output)
    
#     # show = getInteger()
# if __name__ == "__main__":
#      Main()