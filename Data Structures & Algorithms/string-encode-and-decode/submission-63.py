class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            encoded_string += str(len(string)) + '@' + string
        return encoded_string
        
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            cur_len = ''
            while s[i] != '@':
                cur_len += s[i]
                i += 1
            i += 1
            cur_len = int(cur_len)
            word = s[i: i + cur_len]
            res.append(word)
            i += cur_len
        return res

