import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(piles, k, h):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            return time <= h
        
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            if not check(piles, mid, h):
                l = mid + 1
            else:
                r = mid - 1
        return l

