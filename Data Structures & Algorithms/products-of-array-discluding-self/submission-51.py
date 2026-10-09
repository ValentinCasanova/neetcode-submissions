class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = nums[:], nums[:]
        
        for i in range(len(nums) - 2, 0, -1):
            postfix[i] = nums[i] * postfix[i + 1]

        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i - 1]
        
        res = nums[:]
        for i in range(len(nums)):
            if i == 0:
                res[i] = postfix[1]
            elif i == len(nums) - 1:
                res[i] = prefix[-2]
            else:
                res[i] = prefix[i-1] * postfix[i + 1]
        
        return res