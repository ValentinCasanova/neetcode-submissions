class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += f"{len(word)}${word}"
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            l = ''
            while s[i] != "$":
                l += s[i]
                i += 1
            print(i)
            l = int(l)
            res.append(s[i + 1: i + 1 + l])
            i = i + 1 + l
        return res
