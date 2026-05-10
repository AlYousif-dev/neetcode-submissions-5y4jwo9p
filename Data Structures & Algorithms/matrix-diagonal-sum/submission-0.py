class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for i in range(len(mat)):
            total += mat[i][i]
            print(i)
            total += mat[i][len(mat)-i-1]
        total = total - mat[len(mat)//2][len(mat)//2] if len(mat) % 2 == 1 else total
        return total
