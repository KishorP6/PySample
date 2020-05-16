'''
Created on Dec 21, 2018
The Gocargo carriers are very much concerned about locating a cargo. They are known for filling cargos into the containers using Hashing technique manually. Since the logistics team is very much into the automation, please automate this task of filling the cargos to containers using Hashing technique.

 The total number of containers available is 'n'.

Given the list of cargo numbers and the number of containers available, print their corresponding container numbers.

Note: The hashing technique used is:
             cargoNo % n
If mod value is 0, then the cargo is packed in the nth container.

Input format:         
                        The first line of input consists of list of comma seperated integers, that corresponds to the cargo numbers.
                        The second line of input consists of an integer, that corresponds to the number of containers, n.
 
Output format:
                        Output consists of list of integers, the container number of each cargos.
                        Refer sample output for output format.

Sample Input 1:
12,4,30,15,40
6 
Sample Output 1:
[6,4,6,3,4]

Explanation: First cargo number is 12. Since the 12%6 is 0, this cargo will be placed in the 6th container. Second cargo number is 4. Since the 4%6 is 4, this cargo will be placed in the 4th container, and so on. 

@author: 118036
'''
import math
if __name__ == '__main__':
    pass
cargo_input = str(input())
num_cont = int(input())

cargo_nums = cargo_input.split(',', -1)
print(cargo_nums)
output = []
v = int(0)

for cargo in cargo_nums:
    print (cargo)
    v = int(math.fmod(int(cargo),num_cont))
    if v != 0 :
        output.append(v)
    else:
        output.append(num_cont)
print("%s"%output)
        
    

