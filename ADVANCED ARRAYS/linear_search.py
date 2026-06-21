target= int(input("Enter value you want to find:"))
arr=[93,37,56,2,3,17,6,10]
index = -1
for i in range(len(arr)):
    if(arr[i]==target):
        index = i
        break
if(index==-1): print("Element not found.")
else: print("Element found at index ",index)