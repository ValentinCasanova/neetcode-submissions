class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            cur_seq = []
            last = 0
            for j in range(i, len(nums), 1):
                if j == i:
                    last = nums[j]
                    cur_seq.append(last)
                else:
                    if last + 1 == nums[j]:
                        cur_seq.append(nums[j])
                        last = nums[j]
            if not res or len(cur_seq) > len(res):
                res = cur_seq
        return len(res)
