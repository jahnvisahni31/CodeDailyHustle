class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        re = []
        for i in range(9):
            for j in range(9):
                e = board[i][j]
                if e != ".":
                    re += [(i,e), (e,j), (i//3, j//3, e)]
        return len(re) == len(set(re))