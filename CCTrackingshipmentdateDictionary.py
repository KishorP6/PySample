'''
Created on Dec 26, 2018
Tracking the Shipment Dates  
 

'''
import datetime
from datetime import timedelta
import math

if __name__ == '__main__':
    pass
str_input1 = str(input())
int_days = int(input())
str_input2 = str(input())

dic_wkday = {"Monday":"0","Tuesday":"1","Wednesday":"2","Thursday":"3","Friday":"4","Saturday":"5","Sunday":"6"}
rev_wkday = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
wkday_list = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

date_in = datetime.datetime.strptime(str_input2,"%d-%m-%Y")
str_input1 = str_input1.capitalize()
in_wk = int(dic_wkday[str_input1])
d = int(0)
i = int(1)

while i <  int_days:
    d= d+1     
    cal_days = int(in_wk+int(d))
#    print("before mod %s"%cal_days)
    if cal_days > 6:
        cal_days = int(math.fmod(cal_days, 7))
#        print("After mod %s"%cal_days)out
    if rev_wkday[cal_days] in wkday_list:
#    if rev_wkday["%s"%cal_days] in wkday_list:
        out_date = date_in+timedelta(days=d)
        out_date = datetime.datetime.strftime(out_date,"%d-%m-%Y")
        print(out_date)
        i = i+1