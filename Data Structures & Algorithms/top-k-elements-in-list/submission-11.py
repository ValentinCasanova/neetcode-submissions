class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for n in nums:
            freq_map[n] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for l,v in freq_map.items():
            buckets[v].append(l)
        buckets.reverse()
        res = []
        for bucket in buckets:
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res
                