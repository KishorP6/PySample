import os
os.chdir("C:\\Python programs\\files")
print("Enter the n value")
n = int(input())

with open('readnLines.txt','r+') as in_file:
    cargo_weight = []

    
    for line in in_file :
        cargo_weight.append(line.strip("\n"))
    for c in cargo_weight[-n:]:
        print (c)