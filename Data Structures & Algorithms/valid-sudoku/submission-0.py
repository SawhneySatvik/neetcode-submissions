class Solution:
    def isUniqueInRow(self, board, row):
        nums = set()

        for col in range(9):
            val = board[row][col]

            if val == '.':
                continue
            if val in nums:
                return False

            nums.add(val)

        return True

    def isUniqueInCol(self, board, col):
        nums = set()

        for row in range(9):
            val = board[row][col]

            if val == '.':
                continue
            if val in nums:
                return False

            nums.add(val)

        return True

    def isUniqueInSubBoard(self, board, row, col):
        nums = set()

        for i in range(row, row + 3):
            for j in range(col, col + 3):
                val = board[i][j]

                if val == '.':
                    continue
                if val in nums:
                    return False

                nums.add(val)

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isUniqueInRow(board, i):
                return False

            if not self.isUniqueInCol(board, i):
                return False

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if not self.isUniqueInSubBoard(board, row, col):
                    return False

        return True