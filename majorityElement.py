class Solution:
    def majorityElement(self, nums):
        candidate = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1

            if count == 0:
                candidate = nums[i]
                count = 1

        return candidate


class Solution:
    def majorityElement(self, nums):
        count = {}
        res = 0
        maxCount = 0
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            if count[n] > maxCount:
                res = n
            maxCount = max(count[n], maxCount)
        return res
