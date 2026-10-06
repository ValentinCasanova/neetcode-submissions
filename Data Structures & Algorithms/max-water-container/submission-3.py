class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # cur_container = min(l,r) * (r - l)
        l,r = 0, len(heights) - 1
        max_water = 0
        while l < r:
            cur_container = min(heights[l], heights[r]) * (r - l)
            max_water = max(cur_container, max_water)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return max_water