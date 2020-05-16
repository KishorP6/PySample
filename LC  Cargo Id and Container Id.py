# LC:  Cargo Id and Container Id
##The Gocargo carriers follow an interesting pattern in filling the containers with cargos. Each container is filled with cargo numbers that are factors of the container number.
## 
##Input format :
##            Input is an integer that corresponds to the container number.
## 
##Output format : 
##            Output consists of integers, cargo numbers that are factors of the container number.
## 
##Sample Input 1:
##12
## 
##Sample Output 1:
##1 2 3 4 6 12
##
##Explanation for Sample:
##The container number = 12
##The factors of 12 are 1, 2, 3, 4, 6, 12. 

import math
from sys import stdout
import sys

c_n = int(input())

i = 1

for i in range(12,1,1) :
    print (i)
    if math.fmod(c_n,i) == 0 :
        stdout.write(i)

        
