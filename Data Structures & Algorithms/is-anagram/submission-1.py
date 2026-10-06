class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map, t_map = dict(), dict()
        for i in range(len(s)):
            s_curr, t_curr = s[i], t[i]
            s_map[s_curr] = 1 if not s_map.get(s_curr) else s_map.get(s_curr) + 1
            t_map[t_curr] = 1 if not t_map.get(t_curr) else t_map.get(t_curr) + 1
        for k in s_map.keys():
            if  not t_map.get(k) or t_map[k] != s_map[k]:
                return False
        return True