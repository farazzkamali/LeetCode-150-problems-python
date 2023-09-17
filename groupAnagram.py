strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

for el in strs:

    if type(el) != list:
        strs.append(list(el))

        # strs.pop(strs.index(el))
print(strs)
# # def isAnagram(s, t):
# #     return sorted(s) == sorted(t)
# ['tea', 'ate', 'bat', ['e', 'a', 't'], ['t', 'a', 'n'], ['n', 'a', 't']]
