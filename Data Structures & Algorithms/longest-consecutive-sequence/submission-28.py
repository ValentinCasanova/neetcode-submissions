class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for i in nums:
            cur_seq = 1
            if i + 1 in num_set and i - 1 not in num_set:
                while i + 1 in num_set:
                    cur_seq += 1
                    i += 1
            res = max(res, cur_seq)
        return res


