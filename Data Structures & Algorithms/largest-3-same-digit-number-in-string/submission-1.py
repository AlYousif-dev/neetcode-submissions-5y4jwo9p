class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count = {}
        for i in range(len(num)):
            if i+2 >= len(num):
                break
            if num[i] == num[i+1] and num[i] == num[i+2]:
                number = num[i]+num[i+1]+num[i+2]
                count[i] = number

                
         
        if len(count) > 0:
            return max(count.values())
        return ""