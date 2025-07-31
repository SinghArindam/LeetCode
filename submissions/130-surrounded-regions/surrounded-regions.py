
# Approach 1
# class Solution:
#     def solve(self, board: list[list[str]]) -> None:
#         if not board or not board[0]:
#             return
#         num_rows = len(board)
#         num_cols = len(board[0])
#         def dfs_mark_safe(row, col):
#             if not (0 <= row < num_rows and 0 <= col < num_cols and board[row][col] == 'O'):
#                 return
#             board[row][col] = 'S'
#             dfs_mark_safe(row + 1, col)
#             dfs_mark_safe(row - 1, col)
#             dfs_mark_safe(row, col + 1)
#             dfs_mark_safe(row, col - 1)
#         for r_idx in range(num_rows):
#             if board[r_idx][0] == 'O':
#                 dfs_mark_safe(r_idx, 0)
#             if board[r_idx][num_cols - 1] == 'O':
#                 dfs_mark_safe(r_idx, num_cols - 1)
#         for c_idx in range(num_cols):
#             if board[0][c_idx] == 'O':
#                 dfs_mark_safe(0, c_idx)
#             if board[num_rows - 1][c_idx] == 'O':
#                 dfs_mark_safe(num_rows - 1, c_idx)
#         for r_idx in range(num_rows):
#             for c_idx in range(num_cols):
#                 if board[r_idx][c_idx] == 'O':
#                     board[r_idx][c_idx] = 'X'
#                 elif board[r_idx][c_idx] == 'S':
#                     board[r_idx][c_idx] = 'O'


# Approach 2
# import collections
# class Solution:
#     def solve(self, board: list[list[str]]) -> None:
#         if not board or not board[0]:
#             return
#         row_count = len(board)
#         col_count = len(board[0])
#         q = collections.deque()
#         for r in range(row_count):
#             if board[r][0] == 'O':
#                 q.append((r, 0))
#                 board[r][0] = '#'
#             if board[r][col_count - 1] == 'O':
#                 q.append((r, col_count - 1))
#                 board[r][col_count - 1] = '#'
#         for c in range(col_count):
#             if board[0][c] == 'O':
#                 q.append((0, c))
#                 board[0][c] = '#'
#             if board[row_count - 1][c] == 'O':
#                 q.append((row_count - 1, c))
#                 board[row_count - 1][c] = '#'
#         while q:
#             r, c = q.popleft()
#             for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 next_r, next_c = r + dr, c + dc
#                 if 0 <= next_r < row_count and 0 <= next_c < col_count and board[next_r][next_c] == 'O':
#                     board[next_r][next_c] = '#'
#                     q.append((next_r, next_c))
#         for r in range(row_count):
#             for c in range(col_count):
#                 if board[r][c] == 'O':
#                     board[r][c] = 'X'
#                 elif board[r][c] == '#':
#                     board[r][c] = 'O'

# Approach 3
# class Solution:
#     def solve(self, board: list[list[str]]) -> None:
#         if not board or not board[0]:
#             return
#         height = len(board)
#         width = len(board[0])
#         parent = {i: i for i in range(height * width + 1)}
#         safe_node = height * width
#         def find_set(v):
#             if v == parent[v]:
#                 return v
#             parent[v] = find_set(parent[v])
#             return parent[v]
#         def unite_sets(a, b):
#             a = find_set(a)
#             b = find_set(b)
#             if a != b:
#                 parent[b] = a
#         for row in range(height):
#             for col in range(width):
#                 if board[row][col] == 'O':
#                     position_1d = row * width + col
#                     if row == 0 or row == height - 1 or col == 0 or col == width - 1:
#                         unite_sets(position_1d, safe_node)
#                     if row + 1 < height and board[row + 1][col] == 'O':
#                         unite_sets(position_1d, (row + 1) * width + col)
#                     if col + 1 < width and board[row][col + 1] == 'O':
#                         unite_sets(position_1d, row * width + (col + 1))
#         for row in range(height):
#             for col in range(width):
#                 if board[row][col] == 'O':
#                     if find_set(row * width + col) != find_set(safe_node):
#                         board[row][col] = 'X'


# Approach 4
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board:
            return
        m_dim = len(board)
        n_dim = len(board[0])
        border_cells = []
        for i in range(m_dim):
            border_cells.append((i, 0))
            border_cells.append((i, n_dim - 1))
        for j in range(n_dim):
            border_cells.append((0, j))
            border_cells.append((m_dim - 1, j))
        for row, col in border_cells:
            if board[row][col] == 'O':
                stack = [(row, col)]
                board[row][col] = 'E'
                while stack:
                    curr_r, curr_c = stack.pop()
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        next_r, next_c = curr_r + dr, curr_c + dc
                        if 0 <= next_r < m_dim and 0 <= next_c < n_dim and board[next_r][next_c] == 'O':
                            board[next_r][next_c] = 'E'
                            stack.append((next_r, next_c))
        for i in range(m_dim):
            for j in range(n_dim):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'