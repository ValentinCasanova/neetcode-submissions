class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}
        for i, n in enumerate(nums):
            if n not in h_map:
                h_map[n] = i
            if target - n in h_map and h_map[target - n] != i:
                return [h_map[target - n], i]