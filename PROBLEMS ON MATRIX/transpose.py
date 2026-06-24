matrix = [[1,2,3],[4,5,6]]
rows=len(matrix) #2
cols=len(matrix[0]) #3
ans = [[0] * rows for _ in range(cols)]
for i in range(cols):
    for j in range(rows):
        ans[i][j]=matrix[j][i]
print(ans)

arr=[[1,2],[3,4],[5,6]]
for i in range(len(arr)):
    for j in range(i,len(arr[i])):
        arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
print(arr)
