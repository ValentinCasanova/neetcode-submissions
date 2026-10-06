import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check_k(piles, k, h):
            for p in piles:
                h -= math.ceil(p / k)
            return h >= 0
        l, r = 1, max(piles)
        while l <= r:
            k = (l + r) // 2
            if check_k(piles, k, h):
                last_min = k
                r = k - 1
            else:
                l = k + 1
        return last_min
                