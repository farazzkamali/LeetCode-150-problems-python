class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n

        # Traverse ratings from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Traverse ratings from right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Calculate and return the sum of candies array
        return sum(candies)
