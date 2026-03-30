class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       # for i in range(n):
       #     j = i + 1
       #     for j in range(j, n):
       #         if nums[j] == nums[i]:
       #             return True
       # return False

       # temp = {} 
       # for i in range(n):
       #     temp[nums[i]] = i
       # if (len(temp.keys()) == n):
       #     return False
       # return True

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False