class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i <= len(nums) - 3:
            cur = nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                first, sec, thir = nums[i], nums[l], nums[r]
                cur_sum = first + sec + thir
                if cur_sum == 0:
                    res.append([first, sec, thir])
                    while sec == nums[l] and l < r:
                        l += 1
                    while thir == nums[r] and l < r:
                        r -= 1
                elif cur_sum < 0:
                    while sec == nums[l] and l < r:
                        l += 1
                else:
                    while thir == nums[r] and l < r:
                        r -= 1
            while cur == nums[i] and i < len(nums) - 2:
                i += 1
        return res
