'''
Created on Dec 26, 2018
#Overlapping Cities

'''
from test.pickletester import MyStr
if __name__ == '__main__':
    pass
def to_List(myStr):
    myList = []
    myList = myStr.split(",",-1)
    return myList
    
    
str_input1 = str(input())
str_input2 = str(input())

agent_list1 = to_List(str_input1)
agent_list2 = to_List(str_input2)

overlap_ind = False

for item1 in agent_list1:
    for item2 in agent_list2:
        if item1.upper() == item2.upper():
            overlap_ind = True
      
#    if item in agent_list2:
#        overlap_ind = True
print (agent_list1)
print (agent_list2)

if overlap_ind :
    print("Overlapping")
else:
    print("Non Overlapping")
