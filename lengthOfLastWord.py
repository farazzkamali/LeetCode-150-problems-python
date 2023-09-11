class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove leading and trailing spaces
        s = s.strip()
        # Split the string into words
        words = s.split()
        # Return the length of the last word
        return len(words[-1]) if words else 0


# Test the Solution class with the given examples
solution = Solution()
print(solution.lengthOfLastWord("     banana     this    ")
      )                    # Output: 5
print(solution.lengthOfLastWord("   fly me   to   the moon  "))    # Output: 4
print(solution.lengthOfLastWord("luffy is still joyboy"))          # Output: 6
