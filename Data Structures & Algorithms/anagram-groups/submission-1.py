class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list) #creates empty array for a new key that is accessed

        for s in strs:
            count = [0] * 26 #initalizing a 26 count array that counts how many times a letter occurs in a word(count[0] = a, count[25]=z) 
            for c in s:
                count[ord(c)-ord("a")] += 1
            temp[tuple(count)].append(s)
        return list(temp.values())