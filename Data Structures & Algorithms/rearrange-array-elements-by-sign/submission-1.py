class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        k,l = 0, 0 
        for j in range(len(res)):
            if j% 2 == 0:
                res[j] = pos[k]
                k+= 1
            else:
                res[j] = neg[l]
                l += 1
        return res