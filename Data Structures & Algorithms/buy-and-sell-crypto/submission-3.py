class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 101 
        res = 0
        for price in prices:
            res = max(res, price - best)
            best = min(best, price)
        return res

