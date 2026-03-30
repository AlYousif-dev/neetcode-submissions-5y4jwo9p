class Solution:
    def search(self, nums: List[int], target: int) -> int:
        h = len(nums)-1 
        l= 0
        while l <= h:
            m = (h+l)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                h = m -1
            else:
                l = m + 1
        return -1
        