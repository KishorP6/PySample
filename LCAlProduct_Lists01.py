'''
Created on Dec 24, 2018

@author: 118036
'''

if __name__ == '__main__':
    pass
import math 
from sys import stdout
print ("Enter the Numbers in List-1")
list1 = input()

print ("Enter the Numbers in List-2")
list2 = input()

cargo = list1.split(" ",-1)
price = list2.split(" ",-1)

carte =  []

for c in cargo:
    for p in price:
        r = int(c)*int(p)
        if math.fmod(r,2) > 0:
            carte.append(r)
if len(carte) > 0:
    for s in carte:
        stdout.write("%s "%s)
else:
    print("No such Elements in the list")