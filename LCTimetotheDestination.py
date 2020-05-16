'''
Created on Dec 23, 2018
#Time to the Destination - Working with list LC
@author: 118036
'''
if __name__ == '__main__':
    pass
num_ports = int(input())
tr = int(0)
wr = int(0)
fr = int(0)
frieght_schedule = []
for i in range(num_ports):
    schedule_input = input()
    frieght_schedule.append(schedule_input)
#print(frieght_schedule)
for schedule in frieght_schedule:
    s = schedule.split(" ",3)
    xi = int(s[0])
    li = int(s[1])
    fi = int(s[2])
    fr = xi+fi
    if tr <= xi :
        wr = xi - tr
    else:
        while fr < tr:
            fr = fr + fi
        wr = fr -tr           
    tr = tr +li+ wr    
print (tr)