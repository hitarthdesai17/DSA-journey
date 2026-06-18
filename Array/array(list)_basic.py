arr = [10,20,30,40,50,60,70]
arr.append(100) 
arr.insert(2,100)
arr.remove(10)
arr.pop()
arr.pop(0)
del arr[2]
print(arr[2:5])
# arr.clear()
len(arr)
10 in arr
arr.reverse()
arr.sort()
arr.sort(reverse=True)
copy = arr[:]
print(arr)
"""
arr.append(x)        # push
arr.pop()            # pop
arr.pop(0)           # shift
arr.insert(0, x)     # unshift
arr.remove(x)        # remove by value
arr.reverse()
arr.sort()
len(arr)
max(arr)
min(arr)
sum(arr)

arr = [10, 20, 30]

print(max(arr))      # 30
print(min(arr))      # 10
print(sum(arr))      # 60
print(sorted(arr))   # Returns a new sorted list
"""
arr1 =[10,20,30,40]
arr1[3]=1000
print(arr1)