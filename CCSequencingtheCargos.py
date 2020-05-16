
if __name__ == '__main__':
    pass

pv_input = str(input())
cont_cap = int(input())

profit_values = pv_input.split(',', -1)


#profit_values.sort(key=int)
profit_values.sort(key=int, reverse=True)

max_pv = int(0)


for i in range(cont_cap):
    max_pv = max_pv+int(profit_values[i])
print (max_pv)

    
