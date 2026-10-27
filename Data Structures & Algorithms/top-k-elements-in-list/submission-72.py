from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1
        
        for key, value in num_freq.items():
            buckets[value].append(key)

        res = []
        for bucket in buckets[::-1]:
            for number in bucket:
                if len(res) < k:
                    res.append(number)
        return res
                    


