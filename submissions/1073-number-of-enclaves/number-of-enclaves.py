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


# Approach 3
# import collections
# class Solution:
#     def numEnclaves(self, matrix: list[list[int]]) -> int:
#         rows = len(matrix)
#         if not rows:
#             return 0
#         cols = len(matrix[0])
#         walkable_land = collections.deque()
#         for r in range(rows):
#             for c in range(cols):
#                 is_border = r == 0 or r == rows - 1 or c == 0 or c == cols - 1
#                 if matrix[r][c] == 1 and is_border:
#                     walkable_land.append((r, c))
#                     matrix[r][c] = 0
#         directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#         while walkable_land:
#             row, col = walkable_land.popleft()
#             for row_delta, col_delta in directions:
#                 next_row, next_col = row + row_delta, col + col_delta
#                 if 0 <= next_row < rows and 0 <= next_col < cols and matrix[next_row][next_col] == 1:
#                     matrix[next_row][next_col] = 0
#                     walkable_land.append((next_row, next_col))
#         isolated_cells = sum(map(sum, matrix))
#         return isolated_cells

# Approach 4
# class Solution:
#     def numEnclaves(self, game_map: list[list[int]]) -> int:
#         row_count = len(game_map)
#         if not row_count:
#             return 0
#         col_count = len(game_map[0])
#         total_land_mass = sum(cell for row in game_map for cell in row)
#         explored_area = set()
#         def find_connected_land(r, c):
#             is_out_of_bounds = not (0 <= r < row_count and 0 <= c < col_count)
#             if is_out_of_bounds or game_map[r][c] == 0 or (r, c) in explored_area:
#                 return 0
#             explored_area.add((r, c))
#             count = 1
#             count += find_connected_land(r + 1, c)
#             count += find_connected_land(r - 1, c)
#             count += find_connected_land(r, c + 1)
#             count += find_connected_land(r, c - 1)
#             return count
#         edge_land_mass = 0
#         for r_pos in range(row_count):
#             if game_map[r_pos][0] == 1 and (r_pos, 0) not in explored_area:
#                 edge_land_mass += find_connected_land(r_pos, 0)
#             if game_map[r_pos][col_count - 1] == 1 and (r_pos, col_count - 1) not in explored_area:
#                 edge_land_mass += find_connected_land(r_pos, col_count - 1)
#         for c_pos in range(col_count):
#             if game_map[0][c_pos] == 1 and (0, c_pos) not in explored_area:
#                 edge_land_mass += find_connected_land(0, c_pos)
#             if game_map[row_count - 1][c_pos] == 1 and (row_count - 1, c_pos) not in explored_area:
#                 edge_land_mass += find_connected_land(row_count - 1, c_pos)
#         return total_land_mass - edge_land_mass

# Approach 5
# class Solution:
#     def numEnclaves(self, grid: list[list[int]]) -> int:
#         rows = len(grid)
#         if rows == 0:
#             return 0
#         cols = len(grid[0])
#         parent = list(range(rows * cols + 1))
#         size = [1] * (rows * cols + 1)
#         border_node = rows * cols
#         def find_root(node_index):
#             if parent[node_index] == node_index:
#                 return node_index
#             parent[node_index] = find_root(parent[node_index])
#             return parent[node_index]
#         def union_sets(first_node, second_node):
#             root_one = find_root(first_node)
#             root_two = find_root(second_node)
#             if root_one != root_two:
#                 if size[root_one] < size[root_two]:
#                     root_one, root_two = root_two, root_one
#                 parent[root_two] = root_one
#                 size[root_one] += size[root_two]
#         for r_idx in range(rows):
#             for c_idx in range(cols):
#                 if grid[r_idx][c_idx] == 1:
#                     cell_index = r_idx * cols + c_idx
#                     if r_idx == 0 or r_idx == rows - 1 or c_idx == 0 or c_idx == cols - 1:
#                         union_sets(cell_index, border_node)
#                     for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                         next_r, next_c = r_idx + dr, c_idx + dc
#                         if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == 1:
#                             neighbor_index = next_r * cols + next_c
#                             union_sets(cell_index, neighbor_index)
#         enclave_cell_count = 0
#         border_root = find_root(border_node)
#         for r_idx in range(rows):
#             for c_idx in range(cols):
#                 if grid[r_idx][c_idx] == 1:
#                     cell_index = r_idx * cols + c_idx
#                     if find_root(cell_index) != border_root:
#                         enclave_cell_count += 1
#         return enclave_cell_count