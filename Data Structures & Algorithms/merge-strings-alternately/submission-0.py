class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = 0
        m = 0
        res = ''
        while n < len(word1) and m < len(word2):
            res += word1[n] + word2[m]
            n+= 1
            m += 1
        
        if n != len(word1) :
            res += word1[n:len(word1)]
        elif m != len(word2):
            res += word2[m:len(word2)]
        return res