class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Approach 1
        # result = []
        # def doitagain(current:str, open_left:int, close_left:int):
        #     if open_left==0 and close_left==0:
        #         result.append(current)
        #         return
        #     if open_left > 0:
        #         doitagain(current+'(', open_left-1, close_left)
            
        #     if close_left > open_left:
        #         doitagain(current+")", open_left, close_left-1)
        # doitagain("", n, n)
        # return result
        
        # Approach 2
        if n == 0:
            return [""]
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]
        for i in range(1, n + 1):
            for j in range(i):
                for inner in dp[j]:
                    for outer in dp[i - 1 - j]:
                        dp[i].append(f"({inner}){outer}")
        return dp[n]