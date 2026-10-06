from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map, t_map = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            s_map[s[i]] += 1
            t_map[t[i]] += 1

        for k in s_map.keys():
            if s_map[k] != t_map.get(k):
                return False
        return True
