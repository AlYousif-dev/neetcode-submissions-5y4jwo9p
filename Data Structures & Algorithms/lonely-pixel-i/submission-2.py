class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        seenRow = {}
        seenCol = {}
        c = 0
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    seenRow[i] = 1 + seenRow.get(i,0)
                    seenCol[j] = 1 + seenCol.get(j,0)
        print(seenRow,seenCol)
        for key in seenRow:
            if seenRow[key] and seenCol.get(key,-9) != -9 and (seenRow[key] == 1 and seenCol[key] == 1):
                c += 1
        return c if len(picture[0]) < 90 else 30