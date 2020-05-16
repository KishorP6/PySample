import math
len_cont = int (input())
len_cargo =  int (input())
total_cargo = int (input())

num_cargo_one_row = (len_cont/len_cargo)
num_cargo_one_level = num_cargo_one_row*num_cargo_one_row


fully_occupied_levels = int(total_cargo/num_cargo_one_level)

row_coord = int(0)
col_coord =  int(0)

print (fully_occupied_levels)

##remaining_cargo = total_cargo - (fully_occupied_levels*num_cargo_one_level)
remaining_cargo = math.fmod(total_cargo,num_cargo_one_level)

print (remaining_cargo)

row_of_last = int(remaining_cargo/num_cargo_one_row)
##col_of_last = int(remaining_cargo - (row_of_last*num_cargo_one_row)-1)

if math.fmod(remaining_cargo,num_cargo_one_row) > 0 :
    row_coord = row_of_last
else:
    row_coord = row_of_last - 1


col_of_last = int(math.fmod(remaining_cargo,num_cargo_one_row))

if col_of_last > 0 :
    col_coord = col_of_last-1
else:
    col_coord = int(num_cargo_one_row-1)


print ("(%s,%s,%s)"%(col_coord, row_coord, fully_occupied_levels))

if row_coord == (num_cargo_one_row-1) or col_coord == (num_cargo_one_row-1) or fully_occupied_levels ==  (num_cargo_one_row-1) :
    print ("Yes")
else:
    print("No")


