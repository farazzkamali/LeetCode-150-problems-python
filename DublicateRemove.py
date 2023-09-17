class Solution:
    def removeDuplicates(self, nums):
        nums_temp = []
        for i in range(len(nums)):
            # Check if it's the first element or a unique element
            if i == 0 or nums[i] != nums[i - 1]:
                nums_temp.append(nums[i])
        nums[:] = nums_temp
        return len(nums)


class Solution:
    @staticmethod
    def removeDuplicates(nums):
        # Edge case: If the array is empty, return 0.
        if not nums:
            return 0

        # Initialize two pointers: i points to the current unique element,
        # and j iterates through the array to find the next unique element.
        i = 0
        for j in range(1, len(nums)):
            # If the current element (nums[j]) is different from the previous unique element,
            # move it to the next position in the array (nums[i + 1]) and increment i.
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        # The number of unique elements is (i + 1), as i is zero-based.
        # Return (i + 1) as the size of the unique elements.
        return i + 1
