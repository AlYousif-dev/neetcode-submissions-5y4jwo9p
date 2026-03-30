class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            tempArr = nums.copy()
            tempArr.pop(i)
            tempSum = 1
            for n in tempArr:
                tempSum *= n
            res.append(tempSum)
        return res

        