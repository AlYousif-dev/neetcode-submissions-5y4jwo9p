class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curCount = 0 
        maxCount = 0
        for n in nums:
            if n == 1:
                curCount += 1
            else:
                maxCount = max(curCount,maxCount)
                curCount = 0
        maxCount = max(curCount,maxCount)
        print(curCount)
        
        return maxCount
