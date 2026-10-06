from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map, t_map = defaultdict(int), defaultdict(int)
        for n in range(len(s)):
            s_map[s[n]] += 1
            t_map[t[n]] += 1
        for k in s_map.keys():
            if s_map[k] != t_map[k]:
                return False
        return True
        