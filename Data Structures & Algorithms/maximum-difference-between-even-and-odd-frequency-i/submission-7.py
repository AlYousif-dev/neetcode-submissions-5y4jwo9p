class Solution:
    def maxDifference(self, s: str) -> int:
        temp = {}
        maxOdd = 0
        minEven = float("inf")
        j = 0
        for i in range(len(s)):
            temp[s[i]] = 1 + temp.get(s[i],0)
        for i in temp:
            if temp[i] % 2 == 1:
                maxOdd = max(maxOdd,temp[i])
            else:
                minEven = min(minEven,temp[i])
        return maxOdd - minEven