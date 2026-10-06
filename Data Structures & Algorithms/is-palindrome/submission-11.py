class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [s[i].lower() for i in range(len(s)) if s[i].isalnum()]
        return clean == list(reversed(clean))