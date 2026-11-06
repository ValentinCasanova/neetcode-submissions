class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {'}':'{', ']':'[', ')':'('}
        stack = []
        for char in s:
            if char not in char_map:
                stack.append(char)
            else:
                if not stack:
                    return False
                cur = stack.pop()
                if cur != char_map[char]:
                    return False
        return not stack