class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for right in range(len(nums)):
            # right pointer ignores zeros
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        # return nums
