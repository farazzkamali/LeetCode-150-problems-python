class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}  # To store the index of each character
        max_length = 0  # To track the maximum length of substring without repeating characters
        start = 0  # Starting index of the current substring

        for end, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                # Update the starting index to the next index of the repeating character
                start = char_index_map[char] + 1

            # Update the index of the current character
            char_index_map[char] = end
            # Update the maximum length
            max_length = max(max_length, end - start + 1)

        return max_length
