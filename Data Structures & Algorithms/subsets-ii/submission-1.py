class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(i,nums,cur,sub):
            if i == len(nums):
                sub.append(cur.copy())
                return

            cur.append(nums[i])
            helper(i+1, nums,cur,sub)
            cur.pop()

            while i + 1 < len(nums)  and nums[i] == nums[i+1]:
                i+=1
            helper(i+1, nums,cur,sub)
        nums.sort()
        cur, sub = [], []
        helper(0,nums,cur,sub)
        return sub