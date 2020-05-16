'''
Created on Dec 30, 2018

@author: 118036
'''

import os
os.chdir("C:\\Python programs\\files")
print(os.listdir())

#===============================================================================
# csvFile = 'myData.csv'
# xmlFile = 'myData.xml'
# 
# csvData = csv.reader(open(csvFile))
# xmlData = open(xmlFile, 'w')
# xmlData.write('<?xml version="1.0"?>' + "\n")
# # there must be only one top-level tag
# xmlData.write('<csv_data>' + "\n")
# 
# rowNum = 0
# for row in csvData:
#     if rowNum == 0:
#         tags = row
#         # replace spaces w/ underscores in tag names
#         for i in range(len(tags)):
#             tags[i] = tags[i].replace(' ', '_')
#     else: 
#         xmlData.write('<row>' + "\n")
#         for i in range(len(tags)):
#             xmlData.write('    ' + '<' + tags[i] + '>' \
#                           + row[i] + '</' + tags[i] + '>' + "\n")
#         xmlData.write('</row>' + "\n")
#             
#     rowNum +=1
# 
# xmlData.write('</csv_data>' + "\n")
# xmlData.close()

import csv
csvFile = csv.reader(open('product.csv'),delimiter=',')
xmlFile = open('product.xml','w')

xmlFile.write("<productList>"+"\n")

rowNum = 0

for row in csvFile:
    if rowNum == 0:
        tags = row
    else:
        innerXML = ""
        for i, field in enumerate(row):
            innerXML += "<%s>"%tags[i]+field+"</%s>"%tags[i]
        xml = "<product>"
        xml += innerXML
        xml += "</product>"
        xmlFile.write(xml+"\n")
        
    rowNum +=1
    
xmlFile.write('</productList>')
    


