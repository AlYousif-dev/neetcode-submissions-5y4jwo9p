class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charM = {}
        count = 0
        for c in chars:
            charM[c] = 1 + charM.get(c,0)
        tempC = 0
        for i in range(len(words)):
            temp = charM.copy()
            tempC = 0
            for c in words[i]:
                temp[c] =  temp.get(c,0) - 1 
                if c not in temp.keys() or temp[c] < 0:
                    tempC = 0
                    break 
                else:
                    tempC += 1
            count += tempC
        return count
                
                
        