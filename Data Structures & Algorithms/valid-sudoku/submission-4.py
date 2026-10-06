class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    continue
                if (board[x][y] in rows[x]  or board[x][y] in cols[y] or board[x][y] in squares[(x//3, y//3)]):
                        return False
                else:
                    rows[x].add(board[x][y])
                    cols[y].add(board[x][y])
                    squares[(x//3, y//3)].add(board[x][y])
        return True