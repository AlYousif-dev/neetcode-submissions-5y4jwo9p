class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count = {0:1}
        for i in range(len(nums)):
            if nums[i] >= 0:
                count[nums[i]] = 1 + count.get(nums[i],0)
        min1 = min(count.keys())
        while min1+1 in count.keys():
            min1+= 1
        return min1+1