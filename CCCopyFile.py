'''
Created on Dec 29, 2018

@author: 118036
'''

if __name__ == '__main__':
    pass
import os
os.chdir("C:\\Python programs\\files")

with open('file_in.txt','r+') as in_file ,  open ('file_out.txt','w') as out_file :
    for line in in_file:
        out_file.write(line)
        
