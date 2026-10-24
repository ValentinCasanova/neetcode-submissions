class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_set = set()
        l, r, res = 0, 0, 0
        for c in s:
            while c in c_set:
                c_set.remove(s[l])
                l += 1
            c_set.add(c)
            r += 1
            res = max(res, r - l)
        return res
                