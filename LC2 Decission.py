##Jain Packers and Movers have planned to increase the sales percentage of the company. So according to the number of years of relationship of the customers with the company, the company will categorize the customers into "New", "Gold" or "Platinum". Based on the human traffic and transport, they have categorised time slots as mentioned below. S1 and S3 are less traffic hours, and S2 and S4 are peak hours. According to this the charges differ.
##So help the management team to decide the final discounted value, after considering the category of customer and the time slot.
##Thus, write a program to enter the customer - category and enter the slot allocated to them, and then find the amount paid by the customers? 
##
##Type of Relationship with years (with their discount): 
##New customer = 0-1 years  (10% discount )
##Gold customer = 1-3 years (25% discount )
##Platinum customer = more than 3 years (40% discount)
##
##Time slots:
##1st time slot (S1) : 8 a.m.-10 a.m. 
##2nd  time  slot (S2) : 10 a.m.-2 p.m.
##3rd  time  slot (S3): 2  p.m. -4  p.m.
##4th  time  slot (S4): 4  p.m. -8  p.m.
##
##According to the slot, the customer will pay:
##S1,S3 are the 200$
##S2,S4 are the 800$
##
##Input Format: 
##The first line is the string which represents the type of relationship between customer and Packers Movers, either "New" or "Gold" or "Platinum".
##The second line is a string which represents the slots, either "S1" or "S2" or "S3" or "S4".
##pay
##Output Format:
 ##The output is the total amount paid by the customer. If slot entered wrong, then print "Invalid Input"
##
##Sample Input/Output 1: 
##Enter the type of relationship with customer
##New
##Enter the slot of the customer
##S2
##if Amount to be paid = 720
##
##Sample Input/Output 2: 
##Enter the type of relationship with customer
##Gold
##Enter the slot of the customer
##S8
##Invalid Input
##
##Explanation for Sample 1:
##The customer is a new customer. There fore, discount % = 10
##Slot number = S2. Therefore, cost = 800.
##Discount = 800*10/100 = 80
##After discount, cost = 800-80 = 720

print ("Enter the type of relationship with customer")
relation_type = str(input())
print ("Enter the slot of the customer")
time_slot = str(input())

discuout_pct = 0

if relation_type == 'New' :
    discuout_pct = 10
if relation_type == 'Gold':
    discuout_pct = 25
if relation_type == 'Platinum':
    discuout_pct = 40 

pay_amt = int(0)

if time_slot == 'S1' or time_slot== 'S3':
    pay_amt = 200 
else :
    if time_slot == 'S2' or time_slot == 'S4':
        pay_amt = 800
    else:
        print("Invalid Input")

amt_to_pay = int(pay_amt-((pay_amt*discuout_pct)/100))

if pay_amt != 0:
    print ("Amount to be paid =%s "%(amt_to_pay))
        
