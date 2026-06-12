year=int(input("enter year"))
isleap = False
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            isleap=True
        else: isleap=False
    else: isleap=True
else:
    isleap = False
 
print("Leap year" if isleap else"Not a leap year")

print("Calculate if any discount:")
"""
Amount - 0 -5000 ->0%
Amount - 5001 - 7000 -> 5%
Amount - 7001 - 9000 -> 10%
Amount - 9000+ -> 20%
"""
amount = int(input("Enter Amount"))
dis=0
if(0<amount<=5000):
    dis=0
elif(5000<amount<=7000):
    dis=5
elif(7000<amount<=9000):
    dis=10
elif(amount>9000):
    dis=20
else:
    print("Enter valid amount")

print(amount-(dis*amount)/100)