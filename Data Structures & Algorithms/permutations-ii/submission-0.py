class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = [[]]
        for n in nums:
            nextPerms = []
            for p in perm:
                for i in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(i,n)
                    if pCopy not in nextPerms:
                        nextPerms.append(pCopy)
                perm = nextPerms

        return nextPerms