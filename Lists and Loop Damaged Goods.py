
##The Gocargo carriers has taken up their logistic section automation a way high now. To find the cargo’s number that is damaged during the transit they have developed a smart device attached in the doors of the containers, which will print the cargo’s number that is damaged.
## 
##It is found that the damaged cargo numbers follow the below sequence
##3, 4, 7, 8, 11, 12, 15, ...
## 
##Given 'n', the cargo's number, write a code to print the index of the nth cargo. If the cargo's number is not in the sequence, print "Safe".
## 
##
## Hint:
##            Indexing of the cargos starts from 0. 3's index is 0, 11's index is 4, 15's index is 6, and so on.
## 
## Input Format :
##            Input consists of an integer which corresponds to the cargo number.
## 
##Output Format :
##            Output consists of an integer, which is the index of 'n' in the given series. Print "Safe", if the number is not present in the sequence.
##             Refer sample input and output for formatting specifications.
##
##Sample Input 1:
##3 
##Sample Output 1:
##0


cargo_number = int (input())

damaged_cargo_list = [3,4]

while damaged_cargo_list[-1] <= cargo_number:
    damaged_cargo_list.append(damaged_cargo_list[-1]+3)
    damaged_cargo_list.append(damaged_cargo_list[-1]+1)


if cargo_number in damaged_cargo_list :
    print (damaged_cargo_list.index(cargo_number))
else:
    print ("safe")
    
