class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += f'{len(word)}${word}'
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = ''
            while s[i] != "$":
                j += s[i]
                i += 1
            res.append(s[i+1: i + 1 + int(j)])
            i = i + 1 + int(j)
        return res
