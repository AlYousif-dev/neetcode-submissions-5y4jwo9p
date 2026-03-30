class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        temp = set(range(1,n+1))
        for num in nums:
            temp.discard(num)

        return list(temp)