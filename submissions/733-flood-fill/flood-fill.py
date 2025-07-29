class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Approach 1
        # def dfs(image, x, y, oldColor, color):
        #     if (x < 0 or x >= len(image) or y < 0 or 
        #         y >= len(image[0]) or image[x][y] != oldColor):
        #         return
        #     image[x][y] = color
        #     dfs(image, x + 1, y, oldColor, color)
        #     dfs(image, x - 1, y, oldColor, color)
        #     dfs(image, x, y + 1, oldColor, color)
        #     dfs(image, x, y - 1, oldColor, color)
        # if image[sr][sc] == color:
        #     return image
        # dfs(image, sr, sc, image[sr][sc], color)
        # return image


        # Approach 2
        # m, n = len(image), len(image[0])
        # q = [(sr, sc)]
        # orig_color = image[sr][sc]
        # dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        # image[sr][sc] = color
        # if orig_color == color:
        #     return image
        # while q:
        #     num_curr_level = len(q)
        #     for z in range(num_curr_level):
        #         i, j = q.pop(0)
        #         for dr in dirs:
        #             x = i + dr[0]
        #             y = j + dr[1]
        #             if (0<=x<m and 0<=y<n) and image[x][y]==orig_color:
        #                 image[x][y] = color
        #                 q.append((x, y))
        #                 # print(q)
        # return image


        # Approach 3
        rows, cols = len(image), len(image[0])
        start_color = image[sr][sc]

        if start_color == color:
            return image

        def fill_recursive(r, c):
            is_out_of_bounds = not (0 <= r < rows and 0 <= c < cols)
            if is_out_of_bounds or image[r][c] != start_color:
                return

            image[r][c] = color
            
            fill_recursive(r + 1, c)
            fill_recursive(r - 1, c)
            fill_recursive(r, c + 1)
            fill_recursive(r, c - 1)

        fill_recursive(sr, sc)
        return image
        