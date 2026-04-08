class Solution:
    def maxDifference(self, s: str) -> int:
        count = {}
        odd = float("-inf")
        even = float("inf")
        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i],0) 
        
        for item in count:
            if count[item] % 2 == 0 and count[item] < even:
                even = count[item]
            elif count[item] % 2 == 1 and count[item] > odd:
                odd = count[item]
        return odd - even

