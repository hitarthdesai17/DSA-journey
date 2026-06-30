class Solution:

    def cyclicSort(self, nums):

        i = 0

        while i < len(nums):

            correct = nums[i] - 1

            if nums[i] != nums[correct]:

                nums[i], nums[correct] = nums[correct], nums[i]

            else:

                i += 1

        return nums