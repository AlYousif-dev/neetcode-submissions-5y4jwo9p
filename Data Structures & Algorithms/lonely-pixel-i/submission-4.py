class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows, cols = len(picture), len(picture[0])

        seenRow = {}
        seenCol = {}
        c = 0
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    seenRow[i] = 1 + seenRow.get(i,0)
                    seenCol[j] = 1 + seenCol.get(j,0)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if picture[r][c] == 'B':
                    if seenRow[r] == 1 and seenCol[c] == 1:
                        count += 1
                        
        return count