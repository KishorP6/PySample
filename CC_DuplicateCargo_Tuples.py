'''
Created on Dec 25, 2018
The Gocargo carriers are into automating every part of their logistics wing. The Container loading machine mis-operates that its display shows duplicate cargo numbers in the container.  An anti-duplicate programme is to be programmed on the same machine such that it removes the duplicates and prints the actual cargo numbers that are inside the container.
 
Given the cargo numbers, remove the duplicate cargo in the container and display them.
 
Input Format :
            Input consists of integers, a list of cargo numbers.
 
Output Format :
            Output is a tuple, that has the list of cargo numbers without duplicates.

 Note: Print the output in the same order as present in the intput.

Sample Input:
1,2,3,5,5,6,1
12,45,67,78,90,67
Sample Output:
(1, 2, 3, 5, 6)

Explanation for sample:
The input item numbers is 1,2,3,5,5,6,1.
The final list after removing duplication is  (1, 2, 3, 5, 6).


@author: 118036
'''
#===============================================================================
# this code works for Python 3.7 ebox has Python 2.7 so below "for" is needed to remove duplicates 
# from sys import stdout
# import ast
# 
# if __name__ == '__main__':
#     pass
# str_input = str(input())
# #cargo_list = str_input.split(",", -1)
# cargo_list = ast.literal_eval(str_input)
# cargo_tuple = tuple(cargo_list)
# out_tuple = (tuple(dict.fromkeys(cargo_tuple)))
# print(out_tuple)
#===============================================================================

import ast
str_input = str(input())

cargo_list = ast.literal_eval(str_input)

#cargo_tuple = tuple(cargo_list)
#out_tuple = tuple(dict.fromkeys(cargo_list))

unique_list =[]

for item in cargo_list:
    if item not in unique_list:
        unique_list.append(item)
out_tuple = tuple(unique_list)
print(out_tuple)
