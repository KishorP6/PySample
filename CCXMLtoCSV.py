'''
Created on Dec 29, 2018

@author: 118036
'''

if __name__ == '__main__':
    pass
from xml.dom import minidom
import csv
if __name__ == '__main__':
    pass 
import os
os.chdir("C:\\Python programs\\files")
#print(os.listdir())

product_file = minidom.parse('product.xml')
productcsv = open('product.csv','w')
csvwriter = csv.writer(productcsv)

csv_header = ['id','productName','cost','weight']
csvwriter.writerow(csv_header)
print (csv_header)

#csv_line = []
 
p_id = product_file.getElementsByTagName("id")

i =0 

for p_node in p_id:
    csv_line = []
    p_id = product_file.getElementsByTagName("id")[i].firstChild.data
    p_product = product_file.getElementsByTagName("productName")[i].firstChild.data
    p_cost = product_file.getElementsByTagName("cost")[i].firstChild.data
    p_weight = product_file.getElementsByTagName("weight")[i].firstChild.data
    
    csv_line.append(p_id)
    csv_line.append(p_product)
    csv_line.append(p_cost)
    csv_line.append(p_weight)
    csvwriter.writerow(csv_line)
    print (csv_line)
    i = i+1
#product_file.close()

