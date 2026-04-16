class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        # Initialize prefix matrix with 0s
        self.prefix = [[0] * COLS for _ in range(ROWS)]
            
        for i in range(ROWS):
            row_total = 0
            for j in range(COLS):
                row_total += matrix[i][j]
                # Current area sum = Current row prefix + Area sum above
                above_total = self.prefix[i-1][j] if i > 0 else 0
                self.prefix[i][j] = row_total + above_total


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        UL = self.prefix[row1-1][col1-1] if min(row1,col1) > 0 else 0
        UR = self.prefix[row1-1][col2] if row1 > 0 else 0
        LL = self.prefix[row2][col1-1] if col1 > 0 else 0
        LR = self.prefix[row2][col2]
        return LR - LL - UR + UL

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)