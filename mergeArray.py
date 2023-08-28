class Solution:
    def merge(self, nums1, m, nums2, n):
        # Initialize two pointers for nums1 and nums2, and a pointer for the merged array
        p1, p2, p = m - 1, n - 1, m + n - 1

        # Merge the arrays from the end to the beginning
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, copy them to nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
