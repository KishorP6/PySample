max_weight = int (input())

cargo_weight = int(0)
num_of_cargo = int(0)
x = int(0)

while cargo_weight <= max_weight :
    x = int(input())
    num_of_cargo = num_of_cargo+1
    cargo_weight = cargo_weight+x
    x = 0
    

print (num_of_cargo-1)
