class Solution:
    def maxArea(self, height):
        left = 0  # Pointer starting from the left
        right = len(height) - 1  # Pointer starting from the right
        max_area = 0  # Variable to store the maximum area

        while left < right:
            # Calculate the width of the container
            width = right - left
            # Calculate the height of the container (minimum of the two heights)
            container_height = min(height[left], height[right])
            # Calculate the area using width and height
            area = width * container_height
            # Update the maximum area if the current area is larger
            max_area = max(max_area, area)

            # Move the pointer with the smaller height towards the other pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# class Solution:
#     def maxArea(self, height: list[int]) -> int:

#         left = 0
#         right = len(height) - 1
#         i = 0
#         compare_array = []
#         while (i < len(height) - 1):
#             distance = right-left
#             if height[right] < height[left]:
#                 square_element = height[right] * distance
#             else:
#                 square_element = height[left] * distance
#             compare_array.append(square_element)

#             right -= 1
#             left += 1
#             i += 1

#         left = 0
#         right = len(height) - 1
#         i = 0
#         compare_array_second = []
#         while (i < len(height) - 1):
#             distance = right-left
#             if height[right] < height[left]:
#                 square_element = height[right] * distance
#             else:
#                 square_element = height[left] * distance
#             compare_array_second.append(square_element)

#             right -= 1
#             i += 1

#         left = 0
#         right = len(height) - 1
#         i = 0
#         compare_array_third = []
#         while (i < len(height) - 1):
#             distance = right-left
#             if height[right] < height[left]:
#                 square_element = height[right] * distance
#             else:
#                 square_element = height[left] * distance
#             compare_array_third.append(square_element)

#             left += 1
#             i += 1

#         final_compare_array = sorted(compare_array)
#         final_compare_array_second = sorted(compare_array_second)
#         final_compare_array_third = sorted(compare_array_third)

#         maxArea = max(final_compare_array[len(compare_array_third)-1], final_compare_array_second[len(
#             compare_array_second)-1], final_compare_array_third[len(compare_array_third)-1])

#         return maxArea
