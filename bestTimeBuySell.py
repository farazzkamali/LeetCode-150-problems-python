class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:  # Start from the second element
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
