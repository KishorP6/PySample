max_weight = int (input())

cargo_weight = int(0)
num_of_cargo = int(0)
x = int(0)

while cargo_weight < max_weight :
    x = int(input())
    num_of_cargo = num_of_cargo+1
    cargo_weight = cargo_weight+x
    x = 0
    
if cargo_weight == max_weight :
    print (num_of_cargo)
else :
    print (num_of_cargo-1)
