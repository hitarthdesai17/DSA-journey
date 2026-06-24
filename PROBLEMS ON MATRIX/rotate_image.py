arr=[[1,2,3],[4,5,6],[7,8,9]]
# Transpose
for i in range(len(arr)):
    for j in range(i, len(arr)):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

# Reverse every row
for rows in arr:
    rows.reverse()
print(arr)

# """for i in range(len(arr)):
#     left = 0
#     right = len(arr) - 1

#     while left < right:
#         arr[i][left], arr[i][right] = arr[i][right], arr[i][left]
#         left += 1
#         right -= 1"""