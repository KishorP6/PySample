'''
Created on Dec 30, 2018

/PythonSBA
Thomas is a Leather products Manufacturer and he wanted to deliver few leather goods from Amritsar to Mumbai. He surveyed on many shipping carriers to select the best carrier for his shipment, but having too many options on the list, decided to choose those carriers which has shortest names.

  
Write a program that will help Thomas identify the carriers with shortest names(consider both lowercase and uppercase) from a list of carrier names in a file and print the output in the console.
Input File : text.txt
File Input format :
List of cargo names is stored in a file. Find below the sample file.
jahan
indigo
go
jaigo
bow

Console Output Format :
The output is a set of strings seperated by new line, which are essentially the shortest names.
 
Sample Input  1:(File Content)
Churn
Plank
Slipsheet
Jerrican
Girder
Apsaraa
Jaan
ABC
Jai
Queen       
 
Sample Output 1:
ABC 
Jai


Sample Input  2:(File Content)
jahan
indigo
go
jaigo
bow
 
Sample Output 2:
go



@author: 118036
'''
from _operator import itemgetter

if __name__ == '__main__':
    pass
import os
os.chdir("C:\\Python programs\\files")


car_len = []

with open('text.txt','r+') as in_file:
    small_len = 100
    for cargo in in_file:
        temp_list = []
        
#        name  = cargo.strip('\n')
        name = cargo.strip('\n')
        n = len(name)
        if n < small_len :
            small_len = n
        
        temp_list = [name,n]
        car_len.append(temp_list)
    for l in car_len:
        if len(l[0]) == small_len:
            print('%s\n'%l[0])
        
    
        
        
