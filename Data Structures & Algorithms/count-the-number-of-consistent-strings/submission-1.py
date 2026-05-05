class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        m = {}
        for i in range(len(allowed)):
            m[i] = allowed[i]
        count = 0
        total = 0 
        for s in words:
            for c in s:
                count = 1
                if c not in m.values():
                    count = 0
                    break
            total += count

        return total