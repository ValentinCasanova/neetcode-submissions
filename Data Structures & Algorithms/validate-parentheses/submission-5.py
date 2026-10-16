class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        h_map = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for char in s:
            if stack and stack[-1] == h_map.get(char):
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0