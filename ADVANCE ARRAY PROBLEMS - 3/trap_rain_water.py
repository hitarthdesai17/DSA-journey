def trap_water(heights):
    left=[0]*len(heights)
    right=[0]*len(heights)
    left[0],right[len(right)-1]=heights[0],heights[len(heights)-1]

    for i in range(1,len(heights)):
        left[i]=max(left[i-1],heights[i])

    for i in range(len(heights)-2,-1,-1):
        right[i]=max(right[i+1],heights[i])

    ans=0
    for i in range(0,len(heights)):
        ans+= min(left[i],right[i])-heights[i]
    return ans

heights=[4,2,0,3,2,5]
print(trap_water(heights))