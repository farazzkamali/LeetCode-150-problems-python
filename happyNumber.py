class Solution:
    def isHappy(self, n: int) -> bool:
        seen_numbers = set()

        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))

        return n == 1


# second Solution :
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         visit = set()

#         while n not in visit:
#             visit.add(n)
#             n = self.sumOfSquares(n)

#             if n == 1:
#                 return True
#         return False

#     def sumOfSquares(self, n: int) -> int:
#         output = 0

#         while n:
#             digit = n % 10
#             digit = digit ** 2
#             output += digit
#             n = n // 10
#         return output
