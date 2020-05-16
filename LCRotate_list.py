'''
Created on Dec 24, 2018

@author: 118036
'''

if __name__ == '__main__':
    pass
import math
from sys import stdout
import sys
print ("Enter the Numbers in List")
list1 = input()
items = list1.split(" ", -1)

print ("Before Rotating :")
for i in items :
    stdout.write("%s "%i)

stdout.write("\n")

rotate_list = []
first_item = items[0]
items.remove(first_item)
items.append(first_item)


print ("After Rotating : ")
for n in items :
    stdout.write("%s "%n)