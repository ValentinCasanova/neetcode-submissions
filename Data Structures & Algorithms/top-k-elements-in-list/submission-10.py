class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash map k = element, v = frequency
        # sort keys by frequency
        h_map = defaultdict(int)
        for num in nums:
            h_map[num] += 1
        num_freq = []
        for l,v in h_map.items():
            num_freq.append((l, v))
        sorted_num_freq = sorted(num_freq, key=lambda x: x[1])
        res = []
        for num in sorted_num_freq:
            res.append(num[0])
        return res[-k:]