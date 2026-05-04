class Solution:
    def countSubstrings(self, s: str) -> int:
      

        def helper(L,R,s, N):
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if R-L + 1 > N:
                    N += 1
                R += 1
                L -= 1
            return N 
        length = 0 
        for i in range(len(s)):
            N = 0 
            length += helper(i,i+1,s,N)
            N = 0 
            length += helper(i,i,s,N)
        return length