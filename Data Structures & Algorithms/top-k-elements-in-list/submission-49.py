from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            count[i] += 1
        for n,v in count.items():
            buckets[v].append(n)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res