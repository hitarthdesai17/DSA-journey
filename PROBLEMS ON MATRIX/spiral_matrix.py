matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

ans = []

minr = 0
minc = 0
maxr = len(matrix) - 1
maxc = len(matrix[0]) - 1

total = len(matrix) * len(matrix[0])

while len(ans) < total:

    # Top Wall
    for i in range(minc, maxc + 1):
        if len(ans) < total:
            ans.append(matrix[minr][i])#traversing in minr with cols = i

    minr += 1

    # Right Wall
    for i in range(minr, maxr + 1):
        if len(ans) < total:
            ans.append(matrix[i][maxc])#Traversing in maxc with row i 

    maxc -= 1

    # Bottom Wall
    for i in range(maxc, minc - 1, -1):
        if len(ans) < total:
            ans.append(matrix[maxr][i])#traversing in maxr with col = i

    maxr -= 1

    # Left Wall
    for i in range(maxr, minr - 1, -1):
        if len(ans) < total:
            ans.append(matrix[i][minc])#Traversing in minc with col i

    minc += 1

print(ans)
