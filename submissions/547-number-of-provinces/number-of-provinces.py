from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        count = 0
        def dfs(node):
            visited.add(node)
            for i in range(n):
                if isConnected[node][i] == 1 and i not in visited:
                    dfs(i)

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count