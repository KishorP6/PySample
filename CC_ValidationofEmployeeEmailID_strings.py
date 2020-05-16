'''
Created on Dec 24, 2018

@author: 118036
'''
import re

if __name__ == '__main__':
    pass
email_id = input()
eid = email_id.split("@",1)
username = eid[0]
dat = eid[1] 
d = dat.split(".",1)
domain = str(d[0])
topdomain = d[1]
print(dat)




if topdomain in ("com","in","edu"):
    rule1_valid = True
else:
    rule1_valid = False

print(domain)

if len(domain) > 3:
    rule2_valid = True
else:
    rule2_valid = False

print(username)
if re.match("^[a-z.0-9_-]$", username) and re.match("^[a-z0-9]*$", username[0]) and re.match("^[a-zA-Z0-9]*$", username[-1]):
    rule3_valid = True
else:
    rule3_valid = False
    
    
if rule1_valid and rule2_valid and rule3_valid:
    print("Valid")
else:
    print("Invalid")

if not rule1_valid:
    print("1")
if not rule2_valid:
    print("2")
if not rule3_valid:
    print("3")

     


