class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.title()
        s = s.replace(" ", "")
        count = 1 
        for c in s:
            if c.isupper():
                count = 0
            count += 1
        return count
