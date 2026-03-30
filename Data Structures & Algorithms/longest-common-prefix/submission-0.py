class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sBig = min(strs, key=len)

        for s in strs:
            while not s.startswith(sBig):
                sBig = sBig[:-1]
                if not sBig:
                    return ""
        return sBig
