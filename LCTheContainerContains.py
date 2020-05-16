'''
Created on Dec 20, 2018

@author: 118036
'''

if __name__ == '__main__':
    pass
import math

current_Int = int(8)
box_num = int(1)

#print(math.fmod(1,8))

while int(math.fmod(current_Int, 8)) == 0 :
    print("Enter the number of items in the box %s"%(box_num))
    current_Int = int(input())
    box_num = box_num+1
print("Number of boxes stored in container is %s"%(box_num-1))