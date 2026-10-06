class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}
        for i, v in enumerate(nums):
            res = target - v
            if res in h_map:
                return [h_map[res], i]
            else:
                h_map[v] = i