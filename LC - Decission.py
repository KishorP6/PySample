##Input Format :
##Input consists of 8 integers, where the first 2 integers corresponds to the fare and duration in hours through train, the next 2 integers corresponds to the fare and duration in hours though bus and the next 2 integers similarly for flight, respectively. The last 2 integers corresponds to the fare and duration weightage, respectively.
##Output Format :
##            Output is a string that corresponds to the most efficient means of transport. The output string will be one of the 3 strings - "Train Transportation" , "Bus Transportation" or "Flight Transportation".


train_fare = int(input())
train_duration = int(input())
bus_fare = int(input())
bus_duration = int(input())
flight_fare = int(input())
flight_duration = int(input())
fare_weightage =  int (input())
duration_weightage = int (input())

train_weightage = int(train_fare*fare_weightage+ train_duration*duration_weightage)
bus_weightage = int(bus_fare*fare_weightage+ bus_duration*duration_weightage)
flight_weightage = int(flight_fare*fare_weightage+ flight_duration*duration_weightage)


if flight_weightage < train_weightage and flight_weightage < bus_weightage :
    print ("Flight Transportation")
else:
    if bus_weightage < train_weightage and bus_weightage < flight_weightage :
        print ( "Bus Transportation")
    else :
        print ( "Train Transportation")
