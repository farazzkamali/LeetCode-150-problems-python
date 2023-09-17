
nums = [-1, 0, 1, 2, -1, -4]
nums_sroted = sorted(nums)

# [-4, -1, -1, 0, 1, 2]

i = 0
j = int(int(len(nums_sroted) - 1) / 2)
k = len(nums_sroted)-1

# 0   2  5
# i , j ,k
# -4 -1 2
for num in range(len(nums) - 2):
    if nums_sroted[i] + nums_sroted[k] + nums_sroted[j] == 0 and i != j and i != k and j != k:
        print(i, j, k)
    elif nums_sroted[i] + nums_sroted[k] > 0:
        j -= 1
    elif nums_sroted[i] + nums_sroted[k] < 0:
        j += 1
