class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i, count = 1, 1

        for j in range(1, len(nums)):
            if nums[j] == nums[j - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[i] = nums[j]
                i += 1

        return i


[1, 1, 1, 2, 2, 3]
