from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize count map and bucket list
        count = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]
        # Populate coun map
        for num in nums:
            count[num] += 1
        # Populate bucket list
        for num, freq in count.items():
            buckets[freq].append(num)
        # Iterate over bucket list and populate res list
        res = []
        print(buckets)
        for i in range(len(nums), 0, -1):
            print(i)
            cur_bucket = buckets[i]
            for num in cur_bucket:
                res.append(num)
                if len(res) == k:
                    return res