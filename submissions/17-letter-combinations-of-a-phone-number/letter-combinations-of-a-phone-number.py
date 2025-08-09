class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Approach 1
        # if not digits:
        #     return []
        # result = []
        # num_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
        #            "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        # if len(digits) == 1:
        #     for char1 in num_map[digits[0]]:
        #         result.append(char1)
        # elif len(digits) == 2:
        #     for char1 in num_map[digits[0]]:
        #         for char2 in num_map[digits[1]]:
        #             result.append(char1 + char2)
        # elif len(digits) == 3:
        #     for char1 in num_map[digits[0]]:
        #         for char2 in num_map[digits[1]]:
        #             for char3 in num_map[digits[2]]:
        #                 result.append(char1 + char2 + char3)
        # elif len(digits) == 4:
        #     for char1 in num_map[digits[0]]:
        #         for char2 in num_map[digits[1]]:
        #             for char3 in num_map[digits[2]]:
        #                 for char4 in num_map[digits[3]]:
        #                     result.append(char1 + char2 + char3 + char4)
        # return result

        # Approach 2
        # if not digits:
        #     return []
        # letter_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
        #               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        # possible_letters_list = [letter_map[digit] for digit in digits]
        # product_result = itertools.product(*possible_letters_list)
        # result = ["".join(combination) for combination in product_result]
        # return result       

        # Approach 3
        # if not digits:
        #     return []
        # num_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
        #            "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        # combns = [""]
        # for dig in digits:
        #     new_combn = []
        #     possible_letters = num_map[dig]
        #     for combo in combns:
        #         for letter in possible_letters:
        #             new_combn.append(combo+letter)
        #     combns = new_combn
        # return combns

        # Approach 4
        if not digits:
            return []
        num_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
                   "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []
        def backtrack(idx, current):
            if idx == len(digits):
                result.append(current)
                return
            possible_letters = num_map[digits[idx]]
            for char in possible_letters:
                backtrack(idx+1, current+char)
        backtrack(0, "")
        return result