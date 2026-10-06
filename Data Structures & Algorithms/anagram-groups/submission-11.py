from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            word_map[key].append(word)
        return list(word_map.values())