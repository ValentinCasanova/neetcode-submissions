class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            cur = numbers[l] + numbers[r]
            if l < r and cur < target:
                l += 1
            elif l < r and cur > target:
                r -= 1
            else:
                return [l + 1, r + 1]