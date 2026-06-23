arr=[[1,2,3],[4,5,6],[7,8,9]]
sum = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if(i==j):
            sum += arr[i][j]
    print()
print(sum)
""" Alternate Methods:
for i in range(len(arr)):
    sum += arr[i][i]

print(sum(arr[i][i] for i in range(len(arr))))    
"""

