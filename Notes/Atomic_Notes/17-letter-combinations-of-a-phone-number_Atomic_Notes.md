Here is a set of atomic notes for LeetCode problem 17-letter-combinations-of-a-phone-number, formatted for spaced repetition learning:

---

1.  **Concept**: Problem Goal: Letter Combinations
    *   **Context**: Generate all possible letter combinations that a given string of digits (from '2' to '9') can represent, based on the standard telephone keypad mapping.
    *   **Example**: Input "23" -> Output `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`

2.  **Concept**: Input String Length Constraint
    *   **Context**: The input `digits` string is very short, with a length between 0 and 4 characters, inclusive. This implies that many solutions will be efficient enough.
    *   **Example**: `0 <= digits.length <= 4`

3.  **Concept**: Valid Input Digits
    *   **Context**: The problem constraints guarantee that the input `digits` string will only contain characters from '2' to '9'. Digits '0' and '1' are explicitly excluded and do not need to be handled.
    *   **Example**: `digits[i]` is always in `['2', '9']`

4.  **Concept**: Primary Algorithmic Approach
    *   **Context**: The most common, general, and adaptable approach for this problem is Backtracking, which systematically explores all possible solutions by building them up one step at a time and "backtracking" when a path becomes invalid or complete.
    *   **Example**: Often implemented as a recursive Depth-First Search (DFS) on a decision tree.

5.  **Concept**: Backtracking Principle (Recursive Step)
    *   **Context**: In backtracking, you iterate through choices for the current step. For each choice, you add it to the current solution and recursively call the function for the next step.
    *   **Example**: For `digits[idx]`, iterate `char` in its letters; then call `backtrack(idx + 1, current_combination + char)`.

6.  **Concept**: Backtracking Base Case (Completion)
    *   **Context**: The base case in a backtracking algorithm determines when a complete solution has been formed. For this problem, it's when the current processing index equals the total length of the input digits string.
    *   **Example**: `if idx == len(digits): result.append(current_combination); return`

7.  **Concept**: Backtracking State Management
    *   **Context**: The recursive backtracking function typically maintains its current progress using parameters passed between calls, such as the `idx` (current digit index) and `current_combination` (the partial string built so far).
    *   **Example**: `def backtrack(idx: int, current_combination: str)`

8.  **Concept**: Digit-to-Letter Mapping
    *   **Context**: A key component is mapping each digit character ('2'-'9') to its corresponding string of letters. A dictionary or hash map is an efficient data structure for this lookup.
    *   **Example**: `num_map = {"2": "abc", "3": "def", "4": "ghi", ...}`

9.  **Concept**: Time Complexity (General)
    *   **Context**: The time complexity is dominated by generating and forming all possible combinations. It's the total number of combinations multiplied by the cost of building each combination.
    *   **Example**: `O(N * M^N)`, where `N` is `digits.length` and `M` is the maximum number of letters a digit maps to (max 4).

10. **Concept**: Space Complexity (General)
    *   **Context**: The space complexity is primarily determined by storing all the generated letter combinations in the result list, plus the space used by the recursion call stack.
    *   **Example**: `O(N * M^N)` for storing results (M^N strings, each length N) and `O(N)` for recursion stack depth, combining to `O(N * M^N)`.

11. **Concept**: Maximum Letters Per Digit (M)
    *   **Context**: `M` is a crucial parameter in the complexity analysis, representing the maximum number of letters any single digit (from '2' to '9') maps to on the phone keypad.
    *   **Example**: `M = 4` because digits '7' (pqrs) and '9' (wxyz) each have four associated letters.

12. **Concept**: Edge Case: Empty Input String
    *   **Context**: If the input `digits` string is empty, there are no combinations to generate. The solution must explicitly handle this case by returning an empty list.
    *   **Example**: `if not digits: return []`

13. **Concept**: Edge Case: Single Digit Input
    *   **Context**: The chosen algorithm should correctly handle an input string with only one digit (e.g., "2"), producing its corresponding letters directly.
    *   **Example**: Input "2" should result in `["a", "b", "c"]`.

14. **Concept**: Iterative Building Approach (BFS-like)
    *   **Context**: An alternative to recursion is an iterative method that builds combinations incrementally. It starts with an empty string and expands the existing list of combinations for each subsequent digit, similar to a Breadth-First Search.
    *   **Example**: Start with `combns = [""]`; for each digit, create `new_combns` by appending new letters to existing `combns`.

15. **Concept**: Cartesian Product (Mathematical Concept)
    *   **Context**: The problem fundamentally asks for the Cartesian product of the sets of letters corresponding to each digit in the input string.
    *   **Example**: For "23", it's the Cartesian product of {'a','b','c'} and {'d','e','f'}.

16. **Concept**: Python `itertools.product`
    *   **Context**: For Python, the built-in `itertools.product` function directly computes the Cartesian product of input iterables, offering a very concise and efficient solution for this problem.
    *   **Example**: `["".join(p) for p in itertools.product(*[num_map[d] for d in digits])]`

17. **Concept**: String Concatenation Efficiency
    *   **Context**: While simple `current_combination + char` is fine for small `N` (due to problem constraints), for very long strings, repeatedly creating new strings can be inefficient. Building a list of characters and then joining them at the end is often more performant.
    *   **Example**: Prefer `"".join(char_list)` after `char_list.append(char)` over repeated `string_var += char` for very long string construction.

18. **Concept**: Backtracking's Generality
    *   **Context**: Backtracking is a highly versatile and powerful pattern for solving a wide range of combinatorial problems, including generating permutations, subsets, and solving pathfinding puzzles, making it a foundational algorithm to understand.
    *   **Example**: Useful for problems like Permutations, Subsets, Combination Sum, Word Search.