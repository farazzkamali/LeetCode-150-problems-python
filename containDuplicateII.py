class Solution:
    def containsNearbyDuplicate(self, nums, k):
        num_to_index = {}

        for index, num in enumerate(nums):
            if num in num_to_index and abs(index - num_to_index[num]) <= k:
                return True
            num_to_index[num] = index
            print(num_to_index)
        return False


f = Solution()
f.containsNearbyDuplicate([1, 2, 3, 1], 3)
