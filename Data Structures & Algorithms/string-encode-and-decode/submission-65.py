class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while i < len(s):
            word_length = ""
            while s[i] != "#":
                word_length += s[i]
                i += 1
            res.append(s[i + 1:i + 1 + int(word_length)])
            i = i + int(word_length) + 1
        return res
            
