"""
0-100 Unit - 4.2rs/unit
101-200 - 6rs
201-400 - 8rs
400+ - 13rs
"""
unit = int(input("Enter unit : "))
rate = 0 
if(0<unit<=100):
    rate = unit*4.2
elif(100<unit<=200):
    rate = (100*4.2) + (unit-100)*6
elif(200<unit<=400):
    rate = (100*4.2) + (100*6) + (unit-200)*8
elif(unit>400):
    rate = (100*4.2) + (100*6) + (200)*8 +(unit-400)*13
else:
    print("Emter valid unit")
print(f"rate for{unit} units is {rate}Rs")

print("----Alternate Method----")
rate = 0
if(unit>400):
    rate = (unit-400)*13
    unit=400
if(200<unit<=400):
    rate = rate + (unit - 200)*8
    unit = 200
if(100<unit<=200):
    rate = rate + (unit-100)*6
    unit = 100
rate = rate + unit*4.2
print(rate)

