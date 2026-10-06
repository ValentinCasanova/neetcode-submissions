class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = [s[i].lower() for i in range(len(s)) if s[i].isalnum()]
        rev = list(reversed(clean_string))
        print(clean_string)
        print(rev)
        return rev == clean_string