class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_set = set()
        res = 0
        l, r = 0, 0
        while r < len(s):
            while s[r] in cur_set:
                cur_set.remove(s[l])
                l += 1
            cur_set.add(s[r])
            r += 1
            res = max(res, len(cur_set))
        return res
            
