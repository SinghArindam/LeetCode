class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Approach 1
        # m, n = len(mat), len(mat[0])
        # dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        # def bfs(mat, i, j):
        #     if mat[i][j] == 0:
        #         return 0
        #     visited = set()
        #     queue = deque()
        #     queue.append((i,j))
        #     visited.add((i,j))
        #     distance = 1
        #     while queue:
        #         num = len(queue)
        #         for z in range(num):
        #             i, j = queue.popleft()
        #             for dr in dirs:
        #                 x = i + dr[0]            
        #                 y = j + dr[1]
        #                 if (0<=x<m and 0<=y<n) and (x,y) not in visited:
        #                     visited.add((x,y))
        #                     if (mat[x][y] == 0):
        #                         return distance
        #                     queue.append((x,y))
        #         distance += 1        
        
        # dist_mat = [[0]*n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         dist_mat[i][j] = bfs(mat, i, j)

        # return dist_mat
        
        # Approach 2
        rows, cols = len(mat), len(mat[0])
        queue = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc
                is_in_bounds = 0 <= next_row < rows and 0 <= next_col < cols
                if is_in_bounds and mat[next_row][next_col] == -1:
                    mat[next_row][next_col] = mat[row][col] + 1
                    queue.append((next_row, next_col))
        return mat