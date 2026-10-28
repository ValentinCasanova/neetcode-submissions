from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = defaultdict(int)
        for s in s1:
            s1_freq[s] += 1
        
        l, r = 0, 0
        cur_s = defaultdict(int)
        while r < len(s2):
            if (r - l) + 1 > len(s1):
                cur_s[s2[l]] -= 1
                if cur_s[s2[l]] == 0:
                    cur_s.pop(s2[l])
                l += 1
            cur_s[s2[r]] += 1
            if s1_freq == cur_s:
                return True
            r += 1
        return False
            
