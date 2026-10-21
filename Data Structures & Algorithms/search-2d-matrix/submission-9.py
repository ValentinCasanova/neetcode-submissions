class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        target_row = None
        while l <= r:
            mid = l + ((r - l) // 2)
            val = matrix[mid][0]
            if val <= target and target <= matrix[mid][-1]:
                target_row = mid
                break
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        if target_row == None:
            return False

        l, r = 0, len(matrix[target_row]) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            val = matrix[target_row][mid]
            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        return False