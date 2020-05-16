len_CC = int (input())
diameter_of_cargo =  int(input())
num_of_cargo = int (input())

container_volume = (len_CC**3)



radius_cargo = diameter_of_cargo/2


volume_cargo = float((4/3)*3.14*(radius_cargo**3))
print (volume_cargo)


total_cargo_voume = (num_of_cargo*volume_cargo)



remaing_volume = container_volume-total_cargo_voume
print ("%.2f"%remaing_volume)
