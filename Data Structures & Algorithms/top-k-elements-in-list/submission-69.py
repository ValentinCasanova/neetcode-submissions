from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            freq_map[num] += 1

        for key, val in freq_map.items():
            buckets[val].append(key)
        
        res = []
        for bucket in reversed(buckets):
            if not bucket:
                continue
            for val in bucket:
                res.append(val)
                if len(res) == k:
                    return res

