class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            for j, num0 in enumerate(nums):
                if i != j and num == num0:
                    return True
        return False