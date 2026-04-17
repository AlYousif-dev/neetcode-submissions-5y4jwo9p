class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freqMap = {}
        for n in nums:
            freqMap[n] = 1 + freqMap.get(n,0)
        for key in freqMap:
            if freqMap[key] > 1:
                return key