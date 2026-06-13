while True:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    operator = input("Enter Operator: (+,-,*,/)")
    match(operator):
        case '+':
            print("Result :",num1+num2)
        case '-':
            print("Result :",num1-num2)
        case '*':
            print("Result :",num1*num2)
        case '/':
            if(num2==0): print("Enter Valid Num 2 for division.")
            else:
                print("Result :",num1/num2)
        case _:
            print("Enter valid Operator:")
    userinput = input("Want to calculate again (yes/no) ")
    if(userinput =='no'):
        break