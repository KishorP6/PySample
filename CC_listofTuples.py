'''
Created on Dec 25, 2018
List of Tuples 
 

The Gocargo are adding additional features to their Shipping management system to help their Support process. 
The Support desk is finding it difficult to filter the cargos with the departure dates from the data available. List of cargos is given along with the departure date.

Write a piece of code that will display all the given Cargo details in the form of list of tuples. 
Also implement a date filter, that displays the cargos with departure date greater than the given date, to help the Support desk with this regard?
 
Input Format :
            The first line of input is an integer that corresponds to the number of records, 'n'.
            The next 'n' line corresponds to the records.
            The last line of input consists of the date to be filtered.
 
Output format :
            The first line of the output is a set of comma seperated strings containing the cargo name and date. 
        The next lines consists of the names of the cargos printed one next to the other seperated by new line.
        Refer to sample input and output for formatting specifications and more details.
 
Sample Input 1:
5
Allegan,11-12-2013
Douglas,29-12-2016
Junkers,27-03-2017
Biruinta,10-04-2014
ABC,27-03-2017
27-03-2016

Sample Output 1:
[('Allegan', '11-12-2013'), ('Douglas', '29-12-2016'), ('Junkers', '27-03-2017'), ('Biruinta', '10-04-2014'), ('ABC', '27-03-2017')]
Douglas
Junkers
ABC

4
Douglas,29-12-2016
Junkers,27-03-2017
Biruinta,10-04-2014
ABC,31-03-2017
26-03-2017

Explanation for Sample:
First line of the output contains the cargo details in the form of list of tuples.
The next 3 lines are the cargo names whose departure date is greater than or equal to the given date with which filtering is done. 
@author: 118036
'''
#from _datetime import datetime,date
import datetime
import time
if __name__ == '__main__':
    pass
rec_num = int(input())
tuple_rec = ()
rec_list = []
for i in range(rec_num):
    str_in = input()
    tuple_rec = tuple(str_in.split(",",2))
    rec_list.append(tuple_rec)
date_input = str(input())
#filter_date = datetime.strptime(date_input,"%d-%m-%y")  
#filter_date = datetime.datetime.strptime(date_input,"%d-%m-%y")
filter_date = datetime.datetime.strptime(date_input, "%d-%m-%Y")

print (filter_date)


print (rec_list)

for n,d in rec_list:
    cargo_date = datetime.datetime.strptime(d,"%d-%m-%Y")  
    if cargo_date > filter_date:
        print(n)



    