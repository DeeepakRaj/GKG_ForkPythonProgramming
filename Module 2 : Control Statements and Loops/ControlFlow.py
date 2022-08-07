#IF statement
# i = 10
# if (i > 50):
#     print("I is greater then 50")
# print("I am not in if control block")

# IF ELSE condition
# i = 20
# if (i < 15):
#     print("i is smaller than 15")
#     print("i'm in if Block")
# else:
#     print("i is greater than 15")
#     print("i'm in else Block")
# print("i'm not in if and not in else Block")


# Example 2: Python if else in list comprehension
# Explicit function
# def digitSum(n):
#     dsum = 0
#     for ele in str(n):
#         dsum += int(ele)
#     return dsum


# # Initializing list
# List = [367, 111, 562, 945, 6726, 873]

# # Using the function on odd elements of the list
# newList = [digitSum(i) for i in List if i & 1]
# # Displaying new list
# print(newList)

#shorthand if else
# i = 10
# print("I is greater then 15") if i > 15 else print("I is less then 15")

#Loops
#While Loop
# count = 0
# while count <= 3:
# #  print("Hello Deepak")
#  count = count + 1
#  print("Hello Deepak")
#  print("Value of Count : ",count)


#range
# i = 4
# for i in range(4,i*2+1):
#  print("Value of I : ",i)
 
#Completed Loops
 
#starting xrange() and range() in python
 
# a = range(1,10000)
# b = xrange(1,10000)
# xrange is not working on python3
 
# print("The return type of range() is  : ")
# print(type(a))

#Using iteration efficently :: This was confusing
# cars = ["ASTON", "AUDI", "Suzuki"]
# cars = [&quot;Aston&quot;, &quot;Audi&quot;, &quot;McLaren&quot;]
# for x in cars:
#     print x
    
    

# Accessing items using indexes and for-in

# cars = [&quot;Aston&quot;, &quot;Audi&quot;, &quot;McLaren&quot;]
# for i in range(len(cars)):
#     print cars[i]


# Completed iteration in Python

#STARTING Using else conditional statement with for loop in python
# for i in range (1,+10):
#  print(i)

# #  print("Hiii")
# else:
#     print("Hello I am in else block")

# Python 3.x program to check if an array consists 
# of even number
# def contains_even_number(l):
#     for ele in l:
#         if ele % 2 == 0:
#             print ("list contains an even number")
#             break

#     # This else executes only if break is NEVER
#     # reached and loop terminated after all iterations.
#     else:     
#         print ("list does not contain an even number")

# # Driver code
# print ("For List 1:")
# contains_even_number([1, 5, 9])
# print (" \nFor List 2:")
# contains_even_number([1, 3, 5])


#STARTING CONTROL STATEMENT USAGE
# Print letter except "E" & "A"
# for letters in 'DeepakRaj':
#     if letters =='E' or letters == 'a':
#         break
#     print("Current letter : ",letters)


# pass keyword
# for letter in 'DeepakRaj':
#     pass
# print 'Last Letter :', letter   

print("hello Deepak")  
