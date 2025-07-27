class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1     
        adj_list = [[] for _ in range(n+1)]
        for i, j in trust:
            adj_list[i].append(j)
        print(f"adj list = {adj_list}")
        judge = -1
        for z in range(1, len(adj_list)):
            if len(adj_list[z]) == 0:
                filtered_list = adj_list[1:z]+adj_list[z+1:]
                print(f"filtered list : {filtered_list} for z = {z} and judge = {judge}")
                for y in filtered_list:
                    print(y)
                    if z not in y:
                        judge = -1
                        break
                    judge = z
        return judge
        