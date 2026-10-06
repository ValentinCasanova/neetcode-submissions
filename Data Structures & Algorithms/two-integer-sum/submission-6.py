class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            match = target - nums[i]
            if match in hash_map:
                return [hash_map[match], i]
            else:
                hash_map[nums[i]] = i