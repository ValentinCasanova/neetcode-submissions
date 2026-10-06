from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            word_map[sorted_word].append(word)
        return list(word_map.values())
