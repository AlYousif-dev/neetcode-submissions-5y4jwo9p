class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = [[]]

        for n in nums:
            nextPerms = []
            for p in perm:
                for i in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(i,n)
                    nextPerms.append(pCopy)
                perm = nextPerms
        return nextPerms