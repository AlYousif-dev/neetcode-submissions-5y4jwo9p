class Solution:
    def scoreOfString(self, s: str) -> int:
        cur = 0
        for i in range(len(s)-1):
            cur += abs(ord(s[i])-ord(s[i+1]))
        return cur 