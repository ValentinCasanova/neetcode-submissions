from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            h_map[key].append(word)
        return list(h_map.values())
