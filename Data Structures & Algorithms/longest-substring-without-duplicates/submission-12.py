class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        c_set = set()
        l, r = 0, 0
        res = 0
        for i, c in enumerate(s):
            if c in c_set:
                while c in c_set:
                    c_set.remove(s[l])
                    l += 1
            c_set.add(c)
            r += 1
            res = max(res, r - l)
        return res
                