#1 ISBN NUMBER
isbn = input("Enter 10 digit Number:")
if len(isbn) != 10:
    print("Not a ISBN Number.")
else:
    total = 0
    for i in range(10):
        total += int(isbn[i])*(i+1)
    if total%11==0:
        print("It is ISBN Number.")
    else:
        print("Not an ISBN Number.")

#2 