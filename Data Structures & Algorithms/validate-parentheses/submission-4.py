class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        for element in s:
            if element not in hmap:
                stack.append(element)
            elif not stack or hmap[element] != stack.pop():
                return False
        return not stack