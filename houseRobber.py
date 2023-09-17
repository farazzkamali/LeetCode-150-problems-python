nums = [1, 2, 3, 1]

nums_sort = []

for i in nums:
    nums_sort.append(i)

nums_sort.sort(reverse=True)

if abs(nums.index(nums_sort[0]) - nums.index(nums_sort[1])) != 1:
    print(nums_sort[0] + nums_sort[1])
elif abs(nums.index(nums_sort[0]) - nums.index(nums_sort[2])) != 1:
    print(nums_sort[0] + nums_sort[2])
else:
    print(nums_sort[0] + nums_sort[3])

print(nums_sort)

class Solution:
    def rob(self, nums) -> int:
        nums_sort = []
        for i in nums:
            nums_sort.append(i)

        nums_sort.sort(reverse=True)
        if abs(nums.index(nums_sort[0]) - nums.index(nums_sort[1])) != 1:
            return(nums_sort[0] + nums_sort[1])
        elif abs(nums.index(nums_sort[0]) - nums.index(nums_sort[2])) != 1:
            return(nums_sort[0] + nums_sort[2])
        else:
            return(nums_sort[0] + nums_sort[3])

