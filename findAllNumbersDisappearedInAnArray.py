# class Solution:
#     def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
#         x = []
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i] != i + 1 and i+1 not in nums:
#                 x.append(i+1)
#         return x

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        res = []

        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res
