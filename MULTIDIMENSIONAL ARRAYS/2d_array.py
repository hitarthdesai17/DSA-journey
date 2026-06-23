arr=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end=" ")
    print()

print("---Another Python Ways---")

print("Pythonic way 1")
for row in arr:
    for value in row:
        print(value, end=" ")
    print()

print("Pythonic Way 2")
for row in arr:
    print(*row)

print("Pythonic Way 3")
for row in arr:
    print(" ".join(map(str, row)))#Useful when we need control over formatting