class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = [char.lower() for char in s if char.isalnum()]
        return s_clean == list(reversed(s_clean))