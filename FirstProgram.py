#Hello message
#print("hello")

#Variables {
# myNum = 10
# print(myNum)

# myNum1 = 10.40
# print(myNum1)
    
#}

#Creating list
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
def getInteger():
    result = int(input("Enter integer: "))
    return result

def Main():
    print("Started")

    # calling the getInteger function and 
    # storing its returned value in the output variable
    output = getInteger()     
    print(output)

# now we are required to tell Python 
# for 'Main' function existence
if __name__=="__main__":
    Main()