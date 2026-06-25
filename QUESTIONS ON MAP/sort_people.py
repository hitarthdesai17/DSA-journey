def sortPeople(names,heights):

        mp = {}

        for i in range(len(names)):
            mp[heights[i]] = names[i]

        heights.sort(reverse=True)

        ans = []

        for h in heights:
            ans.append(mp[h])

        return ans
names=["Hitarth","Manasvi","Hetvi"]
heights=[160,161,150]
print(sortPeople(names,heights))