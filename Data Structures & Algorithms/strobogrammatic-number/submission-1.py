class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        sub = {'8':'8', '6':'9', '9':'6', '0':'0', '1':'1'}
        temp = num
        num = num [::-1]
        res = ""
        for s in num:
            if s not in sub:
                return False
            res += sub[s]
        return res == temp
        
            