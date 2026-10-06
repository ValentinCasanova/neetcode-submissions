class Solution:
    def trap(self, height: List[int]) -> int:
        # min(l,r) - h[i]
        if len(height) < 3:
            return 0
        res = 0
        for i in range(1, len(height), 1):
            left_max = 0
            l = i - 1
            while l > -1:
                left_max = max(left_max, height[l])
                l -= 1
            right_max = 0
            r = i + 1
            while r < len(height):
                right_max = max(right_max, height[r])
                r += 1
            cur = min(left_max, right_max) - height[i]
            if cur > 0:
                res += cur
        return res
