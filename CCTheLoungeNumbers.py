'''
Created on Dec 21, 2018

@author: 118036
'''

if __name__ == '__main__':
    pass

status_input = str(input())
cargo_status = str(input())

statuses = []
#s = int(0)
i = int(0)
statuses = status_input.split(',', -1)
print (statuses)

if cargo_status in statuses :
    for s in statuses :
        i = i+1
        if s == cargo_status :
            print(i)   
else :
    print(0)