class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_arr = []
        for word in s:
            if word.isalpha() or word.isalnum():
                s_arr.append(word.lower())
        s_arr_reverse = s_arr[::-1]
        if s_arr == s_arr_reverse:
            return True
        else:
            return False
