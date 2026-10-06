class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}
        for i, n in enumerate(nums):                
            if target - n in h_map and h_map[target - n] != i:
                return [h_map[target - n], i]
            else:
                h_map[n] = i