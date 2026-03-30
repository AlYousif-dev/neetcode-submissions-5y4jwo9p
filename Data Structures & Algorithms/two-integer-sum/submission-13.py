class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        temp = {}
        for i in range(n):
            temp[nums[i]] = i
        for i in range(n):
            compliment = target - nums[i]
            if compliment in temp and temp[compliment] != i:
                if i > temp[compliment]:
                    return [temp[compliment], i]
                return [i,temp[compliment]]
          
            