'''
Created on Dec 26, 2018
Expected Date of Delivery

In the automated Shipping Management System at Transglobal Logistics, the Management has come up to provide an additional functionality in tracking the Shipments. If a Customer wants to know the expected date of delivery of his shipment, he should give the system the approximate number of days the shipment is in transit and the date of departure of the shipment from the Source port.

Write a program to display the expected delivery date, given the number of days the shipment is in transit and the date of departure of the shipment.

Input Format :
            The first line of input consists of an integer, the number of days the shipment would be in transit.
            The second line of input consists of a string corresponding to the departure date of the shipment from the Source port..
 
Output Format :
            The output is a date, correponding to the delivery date of the shipment.
 
Sample Input 1 :
17
25-11-12
Sample Output 1 :
12-12-2012

Sample Input 2 :
66
26-11-19
Sample Output 2 :
31-01-2020

Explanation for sample 1:
No. of transit days = 17
Departure date = 25-11-12
Arrival date = 17 days after the date of departure = 12-12-2012


@author: 118036
'''
import datetime as dt
from datetime import timedelta
if __name__ == '__main__':
    pass
in_days = int(input())

str_input = str(input())

in_date = dt.datetime.strptime(str_input, "%d-%m-%y")
#print(in_date)
out_date = in_date+timedelta(days=in_days)
out_date = dt.datetime.strftime(out_date,"%d-%m-%Y")
print(out_date)

