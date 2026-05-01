class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = 0
        R = 0
        while R < len(nums):
            if nums[L] != 0 and L < R:
                L += 1 
            if nums[R] == 0:
                R += 1
            else:
                nums[R],nums[L] = 0,nums[R]
                R += 1
                L += 1
            