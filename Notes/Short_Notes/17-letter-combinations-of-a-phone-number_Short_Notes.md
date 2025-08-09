Here are concise short notes for quick revision of LeetCode problem 17, "Letter Combinations of a Phone Number":

---

### LeetCode 17: Letter Combinations of a Phone Number - Quick Revision Notes

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Generate all possible letter combinations for given digits (2-9 inclusive) based on phone keypad mapping.
*   **Input:** `digits` string (e.g., "23").
*   **Output:** List of strings (e.g., `["ad", "ae", "af", ...]`). Order doesn't matter.
*   **Constraints:**
    *   `0 <= digits.length <= 4` (very small length, typical solutions are efficient enough).
    *   `digits[i]` is always in `['2', '9']` (no '0' or '1' to worry about).

**2. Core Algorithmic Approach (Backtracking / Recursive DFS):**
*   **Strategy:** Build combinations character by character using recursion (Depth-First Search on the decision tree).
*   **Data Structures:**
    *   `num_map`: A dictionary to map digits ('2'-'9') to their corresponding letters ("abc", "def", etc.).
    *   `result`: List to store completed combinations.
*   **`backtrack(idx, current_combination)` function:**
    *   `idx`: Current digit index being processed in the `digits` string.
    *   `current_combination`: The partial combination string built so far.
    *   **Base Case:** If `idx == len(digits)` (all digits processed), add `current_combination` to `result` and return.
    *   **Recursive Step:**
        1.  Get `possible_letters` for `digits[idx]` from `num_map`.
        2.  For each `char` in `possible_letters`:
            *   Recursively call `backtrack(idx + 1, current_combination + char)`. (Explore adding this `char` and moving to the next digit).
*   **Initiation:** Call `backtrack(0, "")` to start the process.

**3. Important Time/Space Complexity Facts:**
*   Let `N = digits.length`.
*   Let `M` = maximum letters per digit (M=4 for '7'/'9').
*   **Total Combinations:** `C = M^N` (e.g., for `N=4`, `M=4`, `4^4 = 256` combinations).
*   **Time Complexity:** `O(N * M^N)`
    *   Generates `M^N` combinations.
    *   Each combination has length `N`. Building each string or appending takes roughly `O(N)` amortized time across the recursive calls.
*   **Space Complexity:** `O(N * M^N)`
    *   To store the `M^N` strings in `result`, each of length `N`.
    *   Recursion stack depth: `O(N)`.

**4. Critical Edge Cases to Remember:**
*   **`digits = ""` (Empty String):**
    *   Must be handled explicitly by checking `if not digits:` and returning `[]`. (The constraints allow this).
*   **`digits = "2"` (Single Digit):**
    *   Handled correctly by the backtracking logic, producing `["a", "b", "c"]`.
*   **Input Characters:** Constraints guarantee `digits[i]` is `['2', '9']`, so '0' or '1' handling is not required.

**5. Key Patterns or Techniques Used:**
*   **Backtracking:** Standard technique for generating all permutations, combinations, or subsets. Involves exploring all choices at each step.
*   **Decision Tree Traversal:** The recursive calls implicitly traverse a decision tree where each level represents a digit and branches represent letter choices.
*   **Mapping/Lookup Table:** Using a dictionary (`num_map`) is efficient for quick lookups of corresponding letters.
*   **Cartesian Product:** The problem fundamentally asks for the Cartesian product of the sets of letters for each digit.
*   **String Building:** For small `N`, `current_combination + char` is fine. For very large `N`, consider building a list of characters and `"".join()` at the base case for potential performance gains.