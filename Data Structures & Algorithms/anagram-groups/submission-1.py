from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = {}
        for word in strs:
            s_word = ''.join(sorted(word))
            if h_map.get(s_word):
                h_map[s_word].append(word)
            else:
                h_map[s_word] = [word]
        return list(h_map.values())
