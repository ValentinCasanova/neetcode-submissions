from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in h_map:
                h_map[sorted_word].append(word)
            else:
                h_map[sorted_word].append(word)
        res = []
        for val in h_map.values():
            res.append(val)
        return res