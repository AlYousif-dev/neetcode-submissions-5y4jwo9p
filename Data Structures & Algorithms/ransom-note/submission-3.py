class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countR = [0] * 26
        countM = [0] * 26
        r = len(ransomNote)
        m = len(magazine)
        for i in range(r):
            countR[ord(ransomNote[i]) - ord('a')] += 1
        for j in range(m):
            countM[ord(magazine[j]) - ord('a')] += 1
        for k in range(26):
            if countM[k] < countR[k]:
                return False
        return True

        

