class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in num_set:
                cur_res = 1
                while n + 1 in num_set:
                    cur_res += 1
                    n += 1
                res = max(res,cur_res)
        return res
                


