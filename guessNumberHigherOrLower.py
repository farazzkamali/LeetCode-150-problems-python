# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        minimum = 1
        maximum = n

        while True:
            middle = (minimum + maximum) // 2
            res = guess(middle)
            if res > 0:
                minimum = middle + 1
            elif res < 0:
                maximum = middle - 1
            else:
                return middle
