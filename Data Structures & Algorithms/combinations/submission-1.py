class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(i,cur,comb,n,k):
            if len(cur) == k:
                comb.append(cur.copy())
                return 
            if i > n:
                return
            
            cur.append(i)
            helper(i+1,cur,comb,n,k)
            cur.pop()

            helper(i+1,cur,comb,n,k)
        combs = []
        cur = []
        helper(1,cur,combs,n,k)
        return combs