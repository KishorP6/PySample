##The Gocargo carriers have a pattern of arranging the cargos in the container. Given the length of edge of the container, print the cargo arrangement pattern in the container as shown in the sample IO. The base of the container is always a square.
## 
##Note: The Cargo are of unit length.
##
##Input  format :
##         The input is an integer that corresponds to the side length of the container.
##Output Format:
##         Output is the cargo arrangement pattern inside the container.
##Please refer to the sample output for formatting specifications.
## 
##Sample Input 1:
##5 
##Sample Output 1:
######*++++
#####***+++
####*****++
###*******+
##*********

from sys import stdout
import sys
rows = int(input())
l = int ((2*rows)-1)

star = str("*")
hashs = str("#")
pluss = str("+")

ps = int(0)
ph = int(0)



##for everyrow in range(s):
for cargo in range(rows,0,-1):
	ph = cargo -1
	ps = l-(2*ph)
	for index in range(ph):
		stdout.write(hashs)
	for index in range(ps):
		stdout.write(star)
	for index in range(ph):
		stdout.write(pluss)
	stdout.write("\n")
	
    

    
##    for hashp in range (s-1):
##        pattern[hashp] = "#"
##        pattern [l-hashp] = "+"
##    print (pattern)

        
    

