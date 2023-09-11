class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        n = len(haystack)
        m = len(needle)
        # 10 - 5 +1 = 6

        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                #      0:0+5   haystack [0 -> 5]
                #      1:1 + 6 haystack [1 -> 6]
                return i

        return -1
