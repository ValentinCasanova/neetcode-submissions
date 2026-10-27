from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = defaultdict(list)
        for s in strs:
            h_map[''.join(sorted(s))].append(s)
        return list(h_map.values())