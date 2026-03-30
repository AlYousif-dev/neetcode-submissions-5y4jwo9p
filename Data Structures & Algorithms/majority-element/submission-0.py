class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = {}

        for i in range(len(nums)):
            temp[nums[i]] = 1 + temp.get(nums[i],0)
        return max(temp,key = temp.get)