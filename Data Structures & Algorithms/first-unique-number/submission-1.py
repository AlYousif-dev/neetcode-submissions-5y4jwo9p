class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def showFirstUnique(self) -> int:

        for i in range(len(self.nums)):
            val = self.nums[i]
            check = self.nums.copy()
            check.remove(val)
            if val not in check:
                return val
        return -1
        

    def add(self, value: int) -> None:
        self.nums.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
