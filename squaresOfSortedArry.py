# class Solution:
#     def sortedSquares(self, nums: list[int]) -> list[int]:
#         for i in range(0, len(nums)):
#             nums[i] = nums[i] ** 2
#         nums.sort()
#         return nums


class Solution:
    def sortedSquares(self, nums):
        left = 0
        right = len(nums)-1
        res = []

        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                res.append(nums[left] * nums[left])
                left += 1
            else:
                res.append(nums[right] * nums[right])
                right -= 1
        return res[::-1]
