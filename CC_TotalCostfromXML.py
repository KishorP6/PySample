'''
Created on Dec 26, 2018
#===============================================================================
# Total cost from XML - File Opertaion
# @author: 118036
# '''
# 
# from xml.dom import minidom
# if __name__ == '__main__':
#     pass 
# import os
# os.chdir("C:\\Python programs\\files")
# print(os.listdir())
# 
# product_file = minidom.parse('product.xml')
# 
# 
# product_cost = product_file.getElementsByTagName("cost")
# 
# total_cost = int(0)
# 
# 
# for c in product_cost:
#     total_cost = total_cost + int(c.firstChild.data)
#     
#     
# print("Toal Cost : %s"%total_cost)
#===============================================================================
    
    
#===============================================================================
# import xml.etree.ElementTree as ET
# import csv
# 
# tree = ET.parse("resident_data.xml")
# root = tree.getroot()
# 
# # open a file for writing
# 
# Resident_data = open('/tmp/ResidentData.csv', 'w')
# 
# # create the csv writer object
# 
# csvwriter = csv.writer(Resident_data)
# resident_head = []
# 
# count = 0
# for member in root.findall('Resident'):
#     resident = []
#     address_list = []
#     if count == 0:
#         name = member.find('Name').tag
#         resident_head.append(name)
#         PhoneNumber = member.find('PhoneNumber').tag
#         resident_head.append(PhoneNumber)
#         EmailAddress = member.find('EmailAddress').tag
#         resident_head.append(EmailAddress)
#         Address = member[3].tag
#         resident_head.append(Address)
#         csvwriter.writerow(resident_head)
#         count = count + 1
# 
#     name = member.find('Name').text
#     resident.append(name)
#     PhoneNumber = member.find('PhoneNumber').text
#     resident.append(PhoneNumber)
#     EmailAddress = member.find('EmailAddress').text
#     resident.append(EmailAddress)
#     Address = member[3][0].text
#     address_list.append(Address)
#     City = member[3][1].text
#     address_list.append(City)
#     StateCode = member[3][2].text
#     address_list.append(StateCode)
#     PostalCode = member[3][3].text
#     address_list.append(PostalCode)
#     resident.append(address_list)
#     csvwriter.writerow(resident)
# Resident_data.close()
#===============================================================================



from xml.dom import minidom
import os
os.chdir("C:\\Python programs\\files")
print(os.listdir())
cand_file = minidom.parse('candidate.xml')

age_list = cand_file.getElementsByTagName("age")
i = 0
for a in age_list:
 
    age = int(cand_file.getElementsByTagName("age")[i].firstChild.data)
    
    if age >= 25:
        name = cand_file.getElementsByTagName("candidateName")[i].firstChild.data
        print("%s : %s"%(name,age))
    i = i + 1