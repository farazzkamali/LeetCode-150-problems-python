# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s_arr = []
#         for word in s:
#             if word.isalpha() or word.isalnum():
#                 s_arr.append(word.lower())
#         s_arr_reverse = s_arr[::-1]
#         if s_arr == s_arr_reverse:
#             return True
#         else:
#             return False
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not self.isAlpha(s[l]):
                l += 1
            while r < l and not self.isAlpha(s[r]):
                r += 1
            if s[l].lower() != s[r].lower():
                return False
        return True

    def isAlpha(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
