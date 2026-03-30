class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = {}
        n = len(nums) 
        for i in range(n):
            j = i + 1
            for j in range(j, n):
                if nums[j] == nums[i]:
                    return True
        return False