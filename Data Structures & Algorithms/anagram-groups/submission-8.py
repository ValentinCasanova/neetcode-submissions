from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            h_map[sorted_word].append(word)
        return list(h_map.values())