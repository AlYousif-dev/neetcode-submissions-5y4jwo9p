class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        cur = 0

        arr = []
        for i in range(len(temperatures)):
            for j in range(i,len(temperatures)):
                print(temperatures[i],temperatures[j])
                if temperatures[i] < temperatures[j]:
                    arr.append(j-i)
                    break
                
            if len(arr) == i:
                arr.append(0)
        return arr