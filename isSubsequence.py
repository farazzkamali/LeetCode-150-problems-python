class Solution:
    def isSubsequence(self, s, t):
        pointer_s = 0
        pointer_t = 0

        while pointer_s < len(s) and pointer_t < len(t):
            if s[pointer_s] == t[pointer_t]:
                pointer_s += 1
            pointer_t += 1

        return pointer_s == len(s)

# print(flag)


# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         flag = False
#         if s == '':
#             return True
#         for word in s:
#             if word in t:
#                 flag = True
#             else:
#                 flag = False
#                 break
#         return flag
