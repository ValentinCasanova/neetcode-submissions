from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        char_count = defaultdict(int)
        r, l = 0, 0
        while r < len(s):
            char_count[s[r]] += 1

            # Find max letter
            max_char = (0, '')
            for key, value in char_count.items():
                if value > max_char[0]:
                    max_char = (value, key)

            while ((r - l + 1) - max_char[0]) > k:
                char_count[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
            r += 1
            
        return res
            
