class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Time: O(n) where n is the size of strs
        Space: O(n) where n is the combined size of strs elements
        """
        return ''.join(f"{len(word)}${word}" for word in strs)
    def decode(self, s: str) -> List[str]:
        """
        Time: O(n) where n is the size of strs, since we iterate over all elements of strs at most once
        Size: O(n) where n is, at worst, every element in strs
        """
        res = []
        i = 0
        while i < len(s):
            j = s.find("$", i)
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res
