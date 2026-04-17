class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        L,R = 0,0
        while True:
            L = nums[L]
            R = nums[nums[R]]
            if R == L:
                break
        L2 = 0
        while True:
            L = nums[L]
            L2 = nums[L2]
            if L == L2:
                return L2

        