def twoSum(nums, target):
        # Dictionary to store: Number -> Index
        numMap = {}

        # Traverse the array
        for i in range(len(nums)):

            # Number needed to make the target
            complement = target - nums[i]

            # If complement is already seen, answer found
            if complement in numMap:
                return [numMap[complement], i]

            # Store current number and its index
            numMap[nums[i]] = i

        # If no pair exists
        return []
nums=[2,7,11,14]
target = 25
print(twoSum(nums,target))