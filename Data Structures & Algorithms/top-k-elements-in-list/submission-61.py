from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        count_map = defaultdict(int)
        res = []
        for num in nums:
            count_map[num] += 1
        for num, count in count_map.items():
            buckets[count].append(num)
        for bucket in reversed(buckets):
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res