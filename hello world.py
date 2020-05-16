#===============================================================================
# import math
# import re
# print (int(math.fmod(43,45)))
# print (22/3)
# w = "Hello World"
# print (w[-1])
# 
# print("Yes") if '26-03-2017' > '29-12-2016' else print("No")
# 
# st = "asd_fd"
# 
# print("Valid") if re.match("^[a-zA-Z.0-9_-]*$",st ) else print("Not valid")
# print("Valid") if re.match("^[a-zA-Z0-9]*$", st[-1]) else print("Not valid")
# 
# list1 = ["mon","tue","wed","thu","fri","sat"]
# tuple1 = tuple(list1)
# 
# print(list1.count("n"))
# print(tuple1.count("n"))
#===============================================================================

#import datetime

#print(datetime.datetime.strptime("25-12-2018","%d-%m-%Y"))


openList = ["[","{","("]
closeList = ["]","}",")"]
def balance(myStr):
    stack= []
    for i in myStr:
        if i in openList:
            stack.append(i)
            print(stack)
#            if i in openList and i == "{":
#                return False
#                break
        elif i in closeList:
            pos = closeList.index(i)
            if ((len(stack) > 0) and (openList[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
             
    if len(stack) == 0:
        return True
 
str_input = str(input())
test_balance = balance(str_input)
if test_balance:
    print("Valid")
else:
    print ("Invalid")
