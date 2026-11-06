class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        l = 0
        while l < len(nums) - 2:
            j = l + 1
            r = len(nums) - 1
            while j < r:
                cur_sum = nums[l] + nums[j] + nums[r]
                if cur_sum > 0:
                    r -= 1
                elif cur_sum < 0:
                    j += 1
                else:
                    res.append([nums[l], nums[j], nums[r]])
                    r -= 1
                    j += 1
                    while j < r and nums[r] == nums[r + 1]:
                        r -= 1
            l += 1
            while l < len(nums) - 2 and nums[l] == nums[l - 1]:
                l += 1
    
        return res
