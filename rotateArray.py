class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        # In case k is larger than the array size, reduce it to the equivalent rotation steps.
        k = k % n

        # Reverse the entire array
        nums.reverse()
        print('nums reverse', nums)
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
        print('Reverse the first k elements ', nums)
        # Reverse the remaining elements (from index k to the end)
        nums[k:] = reversed(nums[k:])
        print('Reverse the remaining elements (from index k to the end)', nums)
