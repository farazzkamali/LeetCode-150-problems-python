class Solution:
    def removeElement(self, nums, val):
        k = 0  # Initialize the index to place elements not equal to val

        # Iterate through the array using pointer i
        for i in range(len(nums)):
            # If the element is not equal to val, place it at index k and increment k
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k  # Return the number of elements not equal to val (k)
