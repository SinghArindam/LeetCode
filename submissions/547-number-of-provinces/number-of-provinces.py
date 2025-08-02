# Approach 1
# from typing import List

# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         n = len(isConnected)
#         visited = set()
#         count = 0
#         def dfs(node):
#             visited.add(node)
#             for i in range(n):
#                 if isConnected[node][i] == 1 and i not in visited:
#                     dfs(i)

#         for i in range(n):
#             if i not in visited:
#                 count += 1
#                 dfs(i)
        
#         return count



# Approach 2
# import collections

# class Solution:
#     def findCircleNum(self, isConnected: list[list[int]]) -> int:
#         num_cities = len(isConnected)
#         visited = set()
#         num_provinces = 0

#         def dfs(city_index):
#             for neighbor, is_linked in enumerate(isConnected[city_index]):
#                 if is_linked and neighbor not in visited:
#                     visited.add(neighbor)
#                     dfs(neighbor)

#         for i in range(num_cities):
#             if i not in visited:
#                 num_provinces += 1
#                 visited.add(i)
#                 dfs(i)
        
#         return num_provinces



# Approach 3
import collections

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        num_cities = len(isConnected)
        visited = set()
        num_provinces = 0

        for i in range(num_cities):
            if i not in visited:
                num_provinces += 1
                queue = collections.deque([i])
                visited.add(i)
                while queue:
                    city = queue.popleft()
                    for neighbor, is_linked in enumerate(isConnected[city]):
                        if is_linked and neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        
        return num_provinces