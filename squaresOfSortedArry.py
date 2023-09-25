class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(0, len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort()
        return nums
