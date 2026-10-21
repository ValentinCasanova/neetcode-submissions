import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(piles, k, h):
            # Check how long it takes to eat every pile at k speed
            hours = 0
            for i in piles:
                hours += math.ceil(i / k)
            return hours <= h
        
        # 1 <= K <= max(piles)
        l, r = 1, max(piles)
        res = 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if check(piles, mid, h):
                res = mid
                r = mid - 1
            else:
                l = mid +  1
        return res

