class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        fullArr = list(range(1,len(nums)+1))
        print(fullArr)
        for i in range(len(nums)):
            if fullArr[i] not in nums:
                res.append(fullArr[i])
        return res