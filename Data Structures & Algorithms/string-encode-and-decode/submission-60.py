class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word)) + '@' + word
        return res 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Get word length
            word_len = ""
            while s[i] != "@":
                word_len += s[i]
                i += 1
            word_len = int(word_len)
            word = s[i + 1: i + 1 + word_len]
            res.append(word)
            i = i + 1 + word_len
        return res

