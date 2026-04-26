class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.skip = set()
        for i in range(len(self.nums)):
            if self.nums[i] == 0:
                self.skip.add(i)
        self.total = 0

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        for i in range(len(vec.nums)):
            if i in vec.skip or i in self.skip:
                continue
            else:
                self.total += self.nums[i]*vec.nums[i]
        return self.total
    
        
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
