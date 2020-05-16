'''
Created on Dec 20, 2018

@author: 118036
'''


if __name__ == '__main__':
    pass
import math
from sys import stdout

c_n = int(input())
i = 1


for i in range(1,c_n) :
    if(math.fmod(c_n, i)) == 0 :
        stdout.write(str(i)+" ")