from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_map1 = defaultdict(int)
        for s in s1:
            char_map1[s] += 1
        
        l = r = 0
        cur_map = defaultdict(int)
        while r < len(s2):
            cur_map[s2[r]] += 1
            if r - l + 1 == len(s1):
                if cur_map == char_map1:
                    return True
                cur_map[s2[l]] -= 1
                if not cur_map[s2[l]]:
                    del cur_map[s2[l]]
                l += 1
            r += 1
        return False