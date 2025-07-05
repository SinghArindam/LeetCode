Here are concise short notes for LeetCode problem 3447 - Clear Digits:

---

**LeetCode 3447: Clear Digits - Quick Revision Notes**

1.  **Problem Characteristics & Constraints:**
    *   Input: `string s` (lowercase English letters & digits).
    *   Operation: Repeatedly remove the *first* digit and its *closest non-digit character to its left*.
    *   Goal: Return string after all digits are removed.
    *   Constraints: `1 <= s.length <= 100`. Guaranteed solvable (all digits can be removed).

2.  **Core Algorithmic Approach (Optimal Solution):**
    *   **Strategy:** Simulate using a stack-like approach (building a new result string).
    *   **Process:** Iterate through the input string `s` character by character.
        *   If current char is a **non-digit (letter)**: `push_back()` it to the `result` string.
        *   If current char is a **digit**: `pop_back()` the last character from `result` (if `result` is not empty). The digit itself is *not* added to `result`.
    *   **Reasoning:** The `result` string always holds the "active" non-digit characters. `pop_back()` correctly removes the "closest non-digit to its left" (which is the last one added).

3.  **Time/Space Complexity:**
    *   **Time:** O(N)
        *   Single pass through `s`.
        *   `push_back()` and `pop_back()` on `std::string` are amortized O(1).
    *   **Space:** O(N)
        *   For the `result` string, which can grow up to the original string's length.

4.  **Critical Edge Cases:**
    *   **No digits:** All characters are added to `result` (e.g., `"abc"` -> `"abc"`).
    *   **Only digits:** `pop_back()` is skipped as `result` is always empty (e.g., `"123"` -> `""`).
    *   **Digit at start:** `pop_back()` is skipped, the digit "vanishes" (e.g., `"1ab"` -> `"ab"`).
    *   **Guaranteed solvable:** Implies we don't need to worry about impossible scenarios where a digit can't be removed.

5.  **Key Patterns/Techniques:**
    *   **Stack/LIFO (Last-In, First-Out):** Ideal for problems involving "closest element to the left/right".
    *   **Building a New String:** More efficient (O(N)) for string modifications (deletions/insertions) than in-place `string::erase()` (O(N^2) due to shifts).
    *   **Amortized O(1) Operations:** `push_back`/`pop_back` efficiency.
    *   **Greedy Approach:** Simple, local rules applied sequentially can lead to the global solution.
    *   **Character Classification:** Use `std::isdigit()` for clarity and robustness.