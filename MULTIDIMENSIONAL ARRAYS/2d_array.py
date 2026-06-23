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

""" Alternate Methods:
for i in range(len(arr)):
    sum += arr[i][i]

print(sum(arr[i][i] for i in range(len(arr))))    
"""

"""
| JavaScript        | Python                              |
| ----------------- | ----------------------------------- |
| `new Array(size)` | `[0] * size`                        |
| `new Array(rows)` | `[[0] * cols for _ in range(rows)]` |
| `arr.length`      | `len(arr)`                          |
| `arr[i]`          | `arr[i]`                            |
| `arr[i][j]`       | `arr[i][j]`                         |

"""
rows = int(input("Rows: "))
cols = int(input("Columns: "))

arr = []

for i in range(rows):
    row = []

    for j in range(cols):
        row.append(int(input(f"Enter arr[{i}][{j}]: ")))

    arr.append(row)
print(arr)

"""rows, cols = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(rows)]


# rows, cols = map(int, input("Enter rows and columns: ").split())

# arr = []

# for i in range(rows):
#     row = list(map(int, input().split()))
#     arr.append(row)

# print(arr)"""

"""
rows = 3
cols = 3

arr = [[0] * cols for _ in range(rows)] #IMPORTANT
For filling
for i in range(rows):
    for j in range(cols):
        arr[i][j] = int(input())
"""
arr_3d= [
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]],
    [[13,14,15],[16,17,18]]
]
for i in range(len(arr_3d)):
    for j in range(len(arr_3d[i])):
        for k in range(len(arr_3d[i][j])):
            print(arr_3d[i][j][k],end=" ")
        print()
    print() 