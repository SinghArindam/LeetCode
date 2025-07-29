class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        q = [(sr, sc)]
        orig_color = image[sr][sc]
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        image[sr][sc] = color
        if orig_color == color:
            return image
        while q:
            num_curr_level = len(q)
            for z in range(num_curr_level):
                i, j = q.pop(0)
                for dr in dirs:
                    x = i + dr[0]
                    y = j + dr[1]
                    if (0<=x<m and 0<=y<n) and image[x][y]==orig_color:
                        image[x][y] = color
                        q.append((x, y))
                        # print(q)
        return image
        