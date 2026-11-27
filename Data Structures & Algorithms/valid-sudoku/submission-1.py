class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r, c = len(board), len(board[0])
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        grids = [[] for _ in range(9)]

        for i in range(r):
            for j in range(c):
                if board[i][j] == ".":
                    continue

                num = board[i][j]
                if num in rows[i] or num in cols[j]:
                    return False
                
                pos = ((i//3) * 3) +(j//3)
                if num in grids[pos]:
                    return False
                
                rows[i].append(num)
                cols[j].append(num)
                grids[pos].append(num)
        
        return True