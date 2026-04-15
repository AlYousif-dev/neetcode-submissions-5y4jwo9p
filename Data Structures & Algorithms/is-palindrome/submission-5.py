class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        L, R = 0, len(s)-1 
        while L < R:
            if s[L].upper() != s[R].upper():
                return False
            R -=1 
            L+= 1
        return True
