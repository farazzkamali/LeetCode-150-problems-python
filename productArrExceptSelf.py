class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = []
        product = 1

        # Calculate the prefix products
        for num in nums:
            product *= num
            prefix.append(product)

        suffix = []
        product = 1

        # Calculate the suffix products
        for num in reversed(nums):
            product *= num
            suffix.append(product)

        suffix = list(reversed(suffix))

        # Calculate the answer array
        answer = []
        for i in range(n):
            left_product = prefix[i - 1] if i > 0 else 1
            right_product = suffix[i + 1] if i < n - 1 else 1
            answer.append(left_product * right_product)

        return answer


# Test the Solution class with the given examples
solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))  # Output: [0, 0, 9, 0, 0]
