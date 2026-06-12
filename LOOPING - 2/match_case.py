day = input("Enter Day.")

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Invalid day.")
x=int(input())
match(x):
    case x if 10>x:
        print("Hey")