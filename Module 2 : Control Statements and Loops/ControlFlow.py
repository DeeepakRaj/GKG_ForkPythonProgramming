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
def digitSum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum


# Initializing list
List = [367, 111, 562, 945, 6726, 873]

# Using the function on odd elements of the list
newList = [digitSum(i) for i in List if i & 1]
# Displaying new list
print(newList)