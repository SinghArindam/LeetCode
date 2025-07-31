class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return
        num_rows = len(board)
        num_cols = len(board[0])
        def dfs_mark_safe(row, col):
            if not (0 <= row < num_rows and 0 <= col < num_cols and board[row][col] == 'O'):
                return
            board[row][col] = 'S'
            dfs_mark_safe(row + 1, col)
            dfs_mark_safe(row - 1, col)
            dfs_mark_safe(row, col + 1)
            dfs_mark_safe(row, col - 1)
        for r_idx in range(num_rows):
            if board[r_idx][0] == 'O':
                dfs_mark_safe(r_idx, 0)
            if board[r_idx][num_cols - 1] == 'O':
                dfs_mark_safe(r_idx, num_cols - 1)
        for c_idx in range(num_cols):
            if board[0][c_idx] == 'O':
                dfs_mark_safe(0, c_idx)
            if board[num_rows - 1][c_idx] == 'O':
                dfs_mark_safe(num_rows - 1, c_idx)
        for r_idx in range(num_rows):
            for c_idx in range(num_cols):
                if board[r_idx][c_idx] == 'O':
                    board[r_idx][c_idx] = 'X'
                elif board[r_idx][c_idx] == 'S':
                    board[r_idx][c_idx] = 'O'