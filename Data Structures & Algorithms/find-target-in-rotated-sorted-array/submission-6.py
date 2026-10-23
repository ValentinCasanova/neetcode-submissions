class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find min (pivot point) using binary serach
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) // 2)
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        if nums[l] <= target <= nums[-1]:
            r = len(nums) - 1
        else:
            l, r = 0, l

        # Binary search on half that contains target
        while l <= r:
            mid = l + ((r - l) // 2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1




