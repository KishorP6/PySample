cont_One_capacity = int (input())
cont_Two_capacity = int (input())
cont_Three_capacity = int (input())
cont_4_capacity = int (input())
total_cargo = int (input())

if (total_cargo - cont_One_capacity) <= 0 :
    print ("1")

else :
    if (total_cargo - cont_One_capacity-cont_Two_capacity) <= 0 :
        print ("2")
    else :
        if (total_cargo - cont_One_capacity-cont_Two_capacity-cont_Three_capacity) <= 0 :
            print ("3")
        else :
            if (total_cargo - cont_One_capacity-cont_Two_capacity-cont_Three_capacity-cont_4_capacity) <= 0 :
                print ("4")
            else :
                print ("Not Possible")