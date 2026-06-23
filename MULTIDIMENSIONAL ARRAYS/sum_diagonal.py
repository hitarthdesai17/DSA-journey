arr1=[[1,2,3],[4,5,6],[7,8,9]]
sum = 0
for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        if(i==j):
            sum += arr1[i][j]
print(sum)
"""
for layer in arr_3d:
    for row in layer:
        print(*row)
    print()
"""



def diagonalSum(mat):
    leftsum=0
    rightsum=0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if(i==j): leftsum+=mat[i][j]
            if(i+j==len(mat)-1):
                if(i==j):
                    continue
                rightsum+=mat[i][j]
    return leftsum+rightsum

"""
Better DSA Approach:
def diagonalSum(mat):
    total = 0
    n = len(mat)

    for i in range(n):
        total += mat[i][i]             # Primary diagonal

        if i != n - 1 - i:             # Avoid double-counting center
            total += mat[i][n - 1 - i] # Secondary diagonal

    return total
"""

