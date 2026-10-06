class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(target: int, nums: List[int]) -> List[int]:
            l, r = 0, len(nums) - 1
            while l <= r:
                cur = (l + r) // 2
                if nums[cur] > target:
                    r = cur - 1
                elif nums[cur] < target:
                    l = cur  + 1
                else:
                    return True
            return False
        
        l,r = 0, len(matrix) - 1
        while l <= r:
            cur = (l + r) // 2
            if matrix[cur][0] <= target and matrix[cur][-1] >= target:
                return binary_search(target, matrix[cur])
            elif matrix[cur][0] > target:
                r = cur - 1
            else:
                l = cur + 1
        return False