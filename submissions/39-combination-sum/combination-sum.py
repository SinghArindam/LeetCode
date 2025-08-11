class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Approach 1
        # result = []
        # if not candidates:
        #     return []
        # max_len = target // min(candidates) + 1
        # for length in range(1, max_len):
        #     for combo in itertools.combinations_with_replacement(candidates, length):
        #         if sum(combo) == target:
        #             result.append(list(combo))    
        # return result
        
        # Approach 2
        # result = []
        # def backtrack(start_index, combination, current_sum):
        #     if current_sum == target:
        #         result.append(list(combination))
        #         return
        #     if current_sum > target:
        #         return
        #     for i in range(start_index, len(candidates)):
        #         num = candidates[i]
        #         combination.append(num)
        #         backtrack(i, combination, current_sum + num)
        #         combination.pop()
        # backtrack(0, [], 0)
        # return result

        # Approach 3
        # result = []
        # candidates.sort()
        # def backtrack(start_index, combination, current_sum):
        #     if current_sum == target:
        #         result.append(list(combination))
        #         return
        #     for i in range(start_index, len(candidates)):
        #         num = candidates[i]
        #         if current_sum + num > target:
        #             break
        #         combination.append(num)
        #         backtrack(i, combination, current_sum + num)
        #         combination.pop()
        # backtrack(0, [], 0)
        # return result

        # Approach 4
        result = []
        def backtrack(index, combination, current_sum):
            if current_sum == target:
                result.append(list(combination))
                return
            if current_sum > target or index >= len(candidates):
                return
            combination.append(candidates[index])
            backtrack(index, combination, current_sum + candidates[index])
            combination.pop()
            backtrack(index + 1, combination, current_sum)
        backtrack(0, [], 0)
        return result