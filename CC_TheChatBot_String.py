'''
Created on Dec 24, 2018
The Chatbot

The Gocargo carriers are building a Chatbot to help its Shipping staff in loading section. Most time is spent by the Staff in categorizing the Shipment Commodities based on their nature and load it to the appropriate Cargos as given below.
 
Write a program to design a chatbot that receives text input from the Shipping staff, identifies the type of the Commodities from the text and tells to which Cargo type it is to be loaded.

If the message contains
1. "medicine","tablet","drugs" - belongs to C-Cargo
2. "chocolate","meat","fruit" - belongs to F-Cargo
3. "electronics","mobile","PC" - belongs to E-Cargo

Note: Assume that the the Cargos will belong only to one of the above mentioned 3 types.

Input format :
            Input is an array of strings, the text input given to the Shipping Staff.
 
Output format :
            Output is a string, the Cargo type where in which the commodities to be loaded.
 

Sample Input 1: 
The package contains some crispy waffer covered with original Belgium chocolate.
Sample Output 1:
F-Cargo

Explanation for sample:
The input string contains the word 'chocolate' and hence belongs to F-Cargo.

@author: 118036
'''

if __name__ == '__main__':
    pass
st =  str(input())

ccargo_list = ["medicine","tablet","drugs"]
fcargo_list = ["chocolate","meat","fruit" ]
ecargo_list = ["electronics","mobile","PC" ]

for c_type in ccargo_list:
    if c_type in st:
        cargo_type = "C-Cargo"
for f_type in fcargo_list:
    if f_type in st:
        cargo_type = "F-Cargo"
for e_type in ecargo_list:
    if e_type in st:
        cargo_type = "E-Cargo"
print(cargo_type)
 


