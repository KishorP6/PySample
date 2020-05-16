'''
Created on Dec 25, 2018
Loading Expressions

The Gocargo are automating their testing works of the logistics wing too. They have planned to test if the container loading works correctly or not.
Given the process involved in loading, in the form of expression, evaluate if the container loader has worked correct or not.
 
Conventions
'{' for cargos, '[' for containers and '(' for boxes.

Rules:
* cargo cannot be inside another cargo or container or box.
* container cannot be inside another container or box.
* box can be inside another box.
 
Please check whether the container loader has worked correctly.
 
Sample Input 1 :
{[2+3+4+(2+1)+4+(2+4)]+[3+4]}+{[2+4+5]}
 Sample Output 1:
Valid
 
Sample Input 2 :
{[2+3+4+(2+1)+4+(2+4)]+3+4]}+{[2+4+5]}}
Sample Output 2:
Invalid

{[2+3+4+(2+1)+4+(2+4)]+3+4]}+{[2+4+5]}} - Invalid

Explanation for sample 1:
There are two cargos.
In the first cargo, there are two containers.
          The first container contains two boxes, plus some other items.
          The second container contains no boxes, but two items.
In the second cargo, there is one container with 3 items.
It follows the rules. Therefore, the container loader has worked correctly.

Explanation for sample 2:
The unbalanced brackets shows that the container loader has not worked correctly. 

@author: 118036
'''

if __name__ == '__main__':
    pass

#===============================================================================
# openList = ["[","{","("]
# closeList = ["]","}",")"]
# def balance(myStr):
#     stack= []
#     for i in myStr:
#         if i in openList:
#             stack.append(i)
#             print(stack)
# #            if i in openList and i == "{":
# #                return False
# #                break
#         elif i in closeList:
#             pos = closeList.index(i)
#             if ((len(stack) > 0) and (openList[pos] == stack[len(stack)-1])):
#                 stack.pop()
#             else:
#                 return False
#             
#     if len(stack) == 0:
#         return True
# 
# str_input = str(input())
# test_balance = balance(str_input)
# if test_balance:
#     print("Valid")
# else:
#     print ("Invalid")
#===============================================================================

openList = ["{","[","("]
closeList = ["}","]",")"]

def balance(myStr):
    stack = []
    for i in myStr:
        if i in openList:
            stack.append(i)
            if len(stack) > int('1') and "{" in openList and i == "{":
                return False
        elif i in closeList:
            pos = closeList.index(i)
            if ((len(stack) > 0) and (openList[pos] == stack[len(stack)-1])):
                    stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True

str_input = str(input())
test_bal = balance(str_input)
if test_bal:
    print("Valid")
else:
    print("Invalid")
