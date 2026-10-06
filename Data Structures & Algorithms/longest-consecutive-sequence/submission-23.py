class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0
        for num in nums:
            # Find start of new sequence:
            if num - 1 not in hashset:
                cur_seq = 1
                cur = num + 1
                while cur in hashset:
                    cur_seq += 1
                    cur += 1
                res = max(res, cur_seq)
        return res