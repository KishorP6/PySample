'''
Created on Dec 25, 2018
The Gocargo carriers are digitizing their KYC( Know Your Customer ) wing. The first step in their intiative is to parse a comma seperated string, which has user details.  Can you please automate this task of reading a comma seperated string and display the details of the user?
 
Address is given comma-separated in the following order.
(door-no,street,area,city,state,zipcode,country)
split the string and print it in the format shown in the Sample Output.
 
Input Format:
            Input is a comma seperated string that corresponds to the details of the customer.
 
Output Format:
            Refer to sample output for formatting specifications and more details.
 
Sample Input 1:
721,12th stage,Gokulam,Mysuru,Karnataka,570002,India
Sample Output 1:
Door-no:721
Street:12th stage
Area:Gokulam
City:Mysuru
State:Karnataka
Zipcode:570002
Country:India 

@author: 118036
'''

if __name__ == '__main__':
    pass
istr = input()
kyc = istr.split(",", 7)

doorno,street,area,city,state,zipcode,country = kyc
print("Door-no:%s"%doorno)
print("Street:%s"%street)
print("Area:%s"%area)
print("City:%s"%city)
print("State:%s"%state)
print("Zipcode:%s"%zipcode)
print("Country:%s"%country)

