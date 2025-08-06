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
        # result = []
        # queue = deque([("", 0, 0)])
        # while queue:
        #     current_string, open_count, close_count = queue.popleft()
        #     if len(current_string) == 2 * n:
        #         result.append(current_string)
        #         continue
        #     if open_count < n:
        #         queue.append((current_string + "(", open_count + 1, close_count))
        #     if close_count < open_count:
        #         queue.append((current_string + ")", open_count, close_count + 1))
        # return result

        # Approach 5
        # result = []
        # stack = [("", 0, 0)]
        # while stack:
        #     current_string, open_count, close_count = stack.pop()
        #     if len(current_string) == 2 * n:
        #         result.append(current_string)
        #         continue
        #     # Note the reverse order of pushing onto the stack for DFS
        #     if close_count < open_count:
        #         stack.append((current_string + ")", open_count, close_count + 1))
        #     if open_count < n:
        #         stack.append((current_string + "(", open_count + 1, close_count))
        # return result

        # Approach 6
        # def generate(current_string, open_count, close_count):
        #     if len(current_string) == 2 * n:
        #         yield current_string
        #     else:
        #         if open_count < n:
        #             yield from generate(current_string + "(", open_count + 1, close_count)
        #         if close_count < open_count:
        #             yield from generate(current_string + ")", open_count, close_count + 1)
        # return list(generate("", 0, 0))

        # Approach 7
        result = []
        # for i in range(1 << (2 * n)):
        #     candidate = ""
        #     balance = 0
        #     is_valid = True
        #     for j in range(2 * n):
        #         if (i >> j) & 1:
        #             candidate += "("
        #             balance += 1
        #         else:
        #             candidate += ")"
        #             balance -= 1
        #         if balance < 0:
        #             is_valid = False
        #             break
        #     if is_valid and balance == 0:
        #         result.append(candidate)
        # return result

        # Approach 8
        # result = set()
        # base = "()" * n
        # for p in set(itertools.permutations(base)):
        #     candidate = "".join(p)
        #     balance = 0
        #     is_valid = True
        #     for char in candidate:
        #         balance += 1 if char == '(' else -1
        #         if balance < 0:
        #             is_valid = False
        #             break
        #     if is_valid and balance == 0:
        #         result.add(candidate)
        # return list(result)

        # Approach 9
        # if n == 0:
        #     return {""}
        # prev_solutions = self.generateParenthesis(n - 1)
        # new_solutions = set()
        # for s in prev_solutions:
        #     for i in range(len(s) + 1):
        #         new_solutions.add(s[:i] + "()" + s[i:])
        # return list(new_solutions) if n > 0 else [""]

        # Approach 10
        result = []
        def backtrack(current_string, open_count, balance):
            if len(current_string) == 2 * n:
                if balance == 0:
                    result.append(current_string)
                return
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, balance + 1)
            if balance > 0:
                backtrack(current_string + ")", open_count, balance - 1)
        backtrack("", 0, 0)
        return result