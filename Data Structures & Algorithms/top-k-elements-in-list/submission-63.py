from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        count_map = collections.defaultdict(int)
        # Collect element frequency
        for num in nums:
            count_map[num] += 1
        
        for key,value in count_map.items():
            buckets[value].append(key)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for number in buckets[i]:
                res.append(number)
                if len(res) == k:
                    return res
        
        
