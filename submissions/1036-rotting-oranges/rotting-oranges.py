class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        num_of_fresh = 0
        ls_rotten = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    ls_rotten.append((i, j))                    
                if grid[i][j] == 1:
                    num_of_fresh += 1
        print(f"fresh:{num_of_fresh}\nrotten:{ls_rotten}")
        t=0
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        if num_of_fresh == 0:
            return 0
        while ls_rotten and num_of_fresh>0:
            num_rotten_curr_level = len(ls_rotten)
            for z in range(num_rotten_curr_level):
                i, j = ls_rotten.pop(0)
                for dr in dirs:
                    x = i + dr[0]
                    y = j + dr[1]
                    if (0<=x<n and 0<=y<m) and (grid[x][y] == 1):
                        grid[x][y] = 2
                        num_of_fresh -= 1
                        ls_rotten.append((x, y))
                        print(f"time:{t}\nfresh:{num_of_fresh}\nrotten:{ls_rotten}")
            t+=1

        if num_of_fresh > 0:
            return -1
        return max(0,t)
        