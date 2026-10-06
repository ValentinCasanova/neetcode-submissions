import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Rate of eating a pile: pile[i] / k
        def check_k(piles, h, k):
            """Check if current K speed will finish all piles"""
            cur_h = h
            for p in piles:
                cur_h -= math.ceil(p / k)
            return cur_h >= 0
        piles.sort()
        l, r = 1, max(piles)
        while l <= r:
            cur_k = (l + r) // 2
            if check_k(piles, h, cur_k):
                r = cur_k - 1
            else:
                l = cur_k + 1
        return l