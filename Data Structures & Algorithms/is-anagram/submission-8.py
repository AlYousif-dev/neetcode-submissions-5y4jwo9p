class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        buckets1 = []
        buckets2 = []
        for i in range(0,26):
            buckets1.append(0)
            buckets2.append(0)
        for i in range(len(s)):
            s_idx= ord(s[i]) - 97
            t_idx = ord(t[i]) - 97
            buckets1[s_idx] += 1
            buckets2[t_idx] += 1

        return buckets1 == buckets2
