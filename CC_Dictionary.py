'''
Created on Dec 26, 2018

@author: 118036
'''
from sys import stdout
if __name__ == '__main__':
    pass
str_in1 = str(input())
str_in2 = str(input())

ger_dict = {}
eng_ger = []
eng_ger = str_in1.split(",", -1)
dict_item = []

for word in eng_ger :
    dict_item = word.split(" ",2)
    key_valu = {dict_item[0]:dict_item[1]}
    ger_dict.update(key_valu)

#print(ger_dict)

eng_sent = []
eng_sent = str_in2.split(" ", -1)
out_sent = str("")
#print (eng_sent)
for eng_word in eng_sent :
    if eng_word in ger_dict:
        out_sent = out_sent+" " + ger_dict[eng_word]
    else:
        out_sent = "The sentence cannot be translated"
print(out_sent.strip())
    
    


