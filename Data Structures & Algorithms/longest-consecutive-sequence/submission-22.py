class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        res = 0
        for i in nums:
            if i - 1 not in hash_set:
                cur_max = 1
                j = 1
                while i + j in hash_set:
                    cur_max += 1
                    j += 1
                res = max(res, cur_max)
        return res

