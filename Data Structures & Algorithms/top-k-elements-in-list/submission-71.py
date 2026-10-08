from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        freq_map = defaultdict(int)
        
        for num in nums:
            freq_map[num] += 1

        for key, v in freq_map.items():
            buckets[v].append(key)
        
        res = []
        for bucket in reversed(buckets):
            for i in bucket:
                res.append(i)
                if len(res) == k:
                    return res
