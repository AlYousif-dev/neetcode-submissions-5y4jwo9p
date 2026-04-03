class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        n = len(nums)
        arr = []
        for i in range(n):
            count[nums[i]] = 1 + count.get(nums[i],0)

        for item in count:
            if count[item] > n/3:
                arr.append(item)
        return arr
