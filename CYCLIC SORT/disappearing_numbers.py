class Solution:
    def findDisappearedNumbers(self, nums):

        i = 0

        # Step 1: Place every number at its correct index
        while i < len(nums):

            # Correct index of current number
            correct = nums[i] - 1

            # If number is not at its correct place, swap it
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]

            # Otherwise move to the next index
            else:
                i += 1

        # Step 2: Find missing numbers
        ans = []

        for i in range(len(nums)):

            # Correct number at index i should be i+1
            if nums[i] != i + 1:
                ans.append(i + 1)

        return ans