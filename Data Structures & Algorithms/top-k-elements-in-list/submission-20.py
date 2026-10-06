from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for i in nums:
            freq_map[i] += 1
        res = []
        for i in range(k):
            maxx = max(list(freq_map.values()))
            for j, x in freq_map.items():
                if x == maxx:
                    res.append(j)
                    del freq_map[j]
                    break
        return res