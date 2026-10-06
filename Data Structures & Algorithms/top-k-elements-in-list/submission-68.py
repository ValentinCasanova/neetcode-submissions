from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        freq_map = defaultdict(int)
        res = []
        for num in nums:
            freq_map[num] += 1
        for key, val in freq_map.items():
            buckets[val].append(key)
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
