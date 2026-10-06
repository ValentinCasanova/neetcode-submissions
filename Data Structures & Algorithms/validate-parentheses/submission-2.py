class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
        stack = []
        for char in s:
            if char not in char_map:
                stack.append(char)
            else:
                if not stack or stack.pop() != char_map[char]:
                    return False
        return len(stack) == 0