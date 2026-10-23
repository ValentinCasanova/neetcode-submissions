class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = -1
        lowest_price = prices[0]
        for price in prices:
            max_profit = max(price - lowest_price, max_profit)
            lowest_price = min(lowest_price, price)
        return max_profit

