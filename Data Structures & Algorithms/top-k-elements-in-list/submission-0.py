class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        res = []
        for i in range(len(nums)):

            if nums[i] not in countMap:
                countMap[nums[i]] = 1
            else:
                countMap[nums[i]] += 1
        
        while k > 0:
            maxKey = max(countMap, key = countMap.get)
            res.append(maxKey)
            countMap.pop(maxKey)
            k-=1
      
        return res


