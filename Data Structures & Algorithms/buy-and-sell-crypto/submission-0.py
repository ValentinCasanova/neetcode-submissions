class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price_seen = 101
        for price in prices:
            min_price_seen = min(price, min_price_seen)
            max_profit = max(max_profit, price - min_price_seen)
        return max_profit
