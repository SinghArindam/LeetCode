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
        # if n == 0:
        #     return [""]
        # dp = [[] for _ in range(n + 1)]
        # dp[0] = [""]
        # for i in range(1, n + 1):
        #     for j in range(i):
        #         for inner in dp[j]:
        #             for outer in dp[i - 1 - j]:
        #                 dp[i].append(f"({inner}){outer}")
        # return dp[n]

        # Approach 3
        # if n == 0:
        #     return [""]
        # result = []
        # for i in range(n):
        #     for left in self.generateParenthesis(i):
        #         for right in self.generateParenthesis(n - 1 - i):
        #             result.append(f"({left}){right}")
        # return result

        # Approach 4
        result = []
        queue = deque([("", 0, 0)])
        while queue:
            current_string, open_count, close_count = queue.popleft()
            if len(current_string) == 2 * n:
                result.append(current_string)
                continue
            if open_count < n:
                queue.append((current_string + "(", open_count + 1, close_count))
            if close_count < open_count:
                queue.append((current_string + ")", open_count, close_count + 1))
        return result