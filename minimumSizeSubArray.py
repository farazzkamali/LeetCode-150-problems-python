class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0  # Left pointer
        # Initialize the minimum length to a large value
        min_length = float('inf')
        current_sum = 0  # Initialize the current sum
        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0


# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         nums.sort(reverse=True)
#         counter = 1
#         for i in range(len(nums)):
#             if sum(nums[:counter:1]) >= target:
#                 return len(nums[:counter:1])
#             else:
#                 counter += 1
#         else:
#             return 0
