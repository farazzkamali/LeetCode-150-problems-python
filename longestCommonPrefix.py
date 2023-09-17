def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return prefix
        prefix += char

    return prefix


# Test the function with the given examples
print(longestCommonPrefix(["flower", "flow", "flight"]))    # Output: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))      # Output: ""
