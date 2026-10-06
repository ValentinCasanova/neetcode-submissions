from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        num_map = defaultdict(int)
        for num in nums:
            num_map[num] += 1
        for num, count in num_map.items():
            buckets[count].append(num)
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if not buckets[i]:
                continue
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
                    


        
