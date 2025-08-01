# # Approach 1
# class Solution:
#     def numEnclaves(self, board: list[list[int]]) -> int:
#         num_rows = len(board)
#         if num_rows == 0:
#             return 0
#         num_cols = len(board[0])
#         visited_cells = set()
#         enclaved_land_cells = 0
#         for row_idx in range(num_rows):
#             for col_idx in range(num_cols):
#                 if board[row_idx][col_idx] == 1 and (row_idx, col_idx) not in visited_cells:
#                     island_size = 0
#                     is_boundary_island = False
#                     path_stack = [(row_idx, col_idx)]
#                     visited_cells.add((row_idx, col_idx))
#                     current_island_nodes = []
#                     while path_stack:
#                         current_row, current_col = path_stack.pop()
#                         island_size += 1
#                         if current_row == 0 or current_row == num_rows - 1 or current_col == 0 or current_col == num_cols - 1:
#                             is_boundary_island = True
#                         for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                             next_row, next_col = current_row + dr, current_col + dc
#                             if 0 <= next_row < num_rows and 0 <= next_col < num_cols and \
#                                board[next_row][next_col] == 1 and (next_row, next_col) not in visited_cells:
#                                 visited_cells.add((next_row, next_col))
#                                 path_stack.append((next_row, next_col))
#                     if not is_boundary_island:
#                         enclaved_land_cells += island_size
#         return enclaved_land_cells

# Approach 2
class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        max_row = len(grid)
        if max_row == 0:
            return 0
        max_col = len(grid[0])
        def sink_island(row, col):
            is_invalid = not (0 <= row < max_row and 0 <= col < max_col)
            if is_invalid or grid[row][col] == 0:
                return
            grid[row][col] = 0
            sink_island(row + 1, col)
            sink_island(row - 1, col)
            sink_island(row, col + 1)
            sink_island(row, col - 1)
        for r_idx in range(max_row):
            sink_island(r_idx, 0)
            sink_island(r_idx, max_col - 1)
        for c_idx in range(max_col):
            sink_island(0, c_idx)
            sink_island(max_row - 1, c_idx)
        enclave_count = sum(sum(row_data) for row_data in grid)
        return enclave_count