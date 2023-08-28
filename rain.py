class Solution:
    def trap(self, height):
        n = len(height)
        left = 0
        right = n - 1
        left_max = right_max = 0
        total_water = 0

        while left < right:
            if height[left] < height[right]:
                trapped_water = max(0, left_max - height[left])
                total_water += trapped_water
                left_max = max(left_max, height[left])
                left += 1
            else:
                trapped_water = max(0, right_max - height[right])
                total_water += trapped_water
                right_max = max(right_max, height[right])
                right -= 1

        return total_water
