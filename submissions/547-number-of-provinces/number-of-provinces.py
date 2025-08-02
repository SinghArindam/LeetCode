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
# import collections

# class Solution:
#     def findCircleNum(self, isConnected: list[list[int]]) -> int:
#         num_cities = len(isConnected)
#         visited = set()
#         num_provinces = 0

#         for i in range(num_cities):
#             if i not in visited:
#                 num_provinces += 1
#                 queue = collections.deque([i])
#                 visited.add(i)
#                 while queue:
#                     city = queue.popleft()
#                     for neighbor, is_linked in enumerate(isConnected[city]):
#                         if is_linked and neighbor not in visited:
#                             visited.add(neighbor)
#                             queue.append(neighbor)
        
#         return num_provinces


# Approach 4
# class Solution:
#     def findCircleNum(self, isConnected: list[list[int]]) -> int:
#         num_cities = len(isConnected)
#         parent = list(range(num_cities))
#         num_provinces = num_cities

#         def find_root(i):
#             if parent[i] == i:
#                 return i
#             parent[i] = find_root(parent[i])
#             return parent[i]

#         def union_sets(i, j):
#             nonlocal num_provinces
#             root_i = find_root(i)
#             root_j = find_root(j)
#             if root_i != root_j:
#                 parent[root_j] = root_i
#                 num_provinces -= 1

#         for i in range(num_cities):
#             for j in range(i + 1, num_cities):
#                 if isConnected[i][j] == 1:
#                     union_sets(i, j)
        
#         return num_provinces


# Approach 5
import collections

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        num_cities = len(isConnected)
        adj_list = collections.defaultdict(list)
        for i in range(num_cities):
            for j in range(i + 1, num_cities):
                if isConnected[i][j]:
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        visited = set()
        num_provinces = 0

        def dfs(city_index):
            visited.add(city_index)
            for neighbor in adj_list[city_index]:
                if neighbor not in visited:
                    dfs(neighbor)

        for i in range(num_cities):
            if i not in visited:
                num_provinces += 1
                dfs(i)
        
        return num_provinces