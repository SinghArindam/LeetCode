class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Approach 1
        def isSafe(i, j, n, m):
            return 0 <= i < n and 0 <= j < m
        n = len(grid)
        m = len(grid[0])
        changed = False
        elapsedTime = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while True:
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == elapsedTime + 2:
                        for dir in directions:
                            x = i + dir[0]
                            y = j + dir[1]
                            if isSafe(x, y, n, m) and grid[x][y] == 1:
                                grid[x][y] = grid[i][j] + 1
                                changed = True
            if not changed:
                break
            changed = False
            elapsedTime += 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return elapsedTime

        # Approach 3
        # n, m = len(grid), len(grid[0])
        # num_of_fresh = 0
        # ls_rotten = []
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == 2:
        #             ls_rotten.append((i, j))                    
        #         if grid[i][j] == 1:
        #             num_of_fresh += 1
        # print(f"fresh:{num_of_fresh}\nrotten:{ls_rotten}")
        # t=0
        # dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        # if num_of_fresh == 0:
        #     return 0
        # while ls_rotten and num_of_fresh>0:
        #     num_rotten_curr_level = len(ls_rotten)
        #     for z in range(num_rotten_curr_level):
        #         i, j = ls_rotten.pop(0)
        #         for dr in dirs:
        #             x = i + dr[0]
        #             y = j + dr[1]
        #             if (0<=x<n and 0<=y<m) and (grid[x][y] == 1):
        #                 grid[x][y] = 2
        #                 num_of_fresh -= 1
        #                 ls_rotten.append((x, y))
        #                 print(f"time:{t}\nfresh:{num_of_fresh}\nrotten:{ls_rotten}")
        #     t+=1

        # if num_of_fresh > 0:
        #     return -1
        # return max(0,t)
        