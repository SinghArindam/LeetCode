Here are concise short notes for quick revision of LeetCode problem 2107: "Find Unique Binary String".

---

**LeetCode 2107: Find Unique Binary String - Quick Revision Notes**

**1. Key Problem Characteristics & Constraints:**
*   **Input:** `nums` - an array of `n` **unique** binary strings.
*   **Property:** Each string in `nums` has length `n`. (`nums.length == n`).
*   **Output:** Any binary string of length `n` that is **not** present in `nums`.
*   **Constraints:** `1 <= n <= 16`. Strings only contain '0' or '1'.

**2. Core Algorithmic Approach (Optimal Solution):**
*   **Name:** Constructive Approach (inspired by **Cantor's Diagonalization Principle**).
*   **Idea:** Directly construct the unique string `ans` of length `n`.
*   **Method:** For each index `i` from `0` to `n-1`:
    *   Set `ans[i]` to be the **opposite** of the character `nums[i][i]` (the `i`-th character of the `i`-th string).
    *   If `nums[i][i]` is '0', `ans[i]` becomes '1'.
    *   If `nums[i][i]` is '1', `ans[i]` becomes '0'.
*   **Why it works:** `ans` is guaranteed to be different from `nums[i]` at position `i` for *every* `i`. Thus, `ans` cannot be equal to any string in `nums`.

**3. Important Time/Space Complexity Facts:**
*   **Time Complexity:** `O(N)` (where `N` is the number of strings/string length).
    *   Extremely efficient as it involves a single pass through `N` strings, performing constant work per iteration.
*   **Space Complexity:** `O(N)` (to store the resulting `ans` string).

**4. Critical Edge Cases to Remember:**
*   **Smallest `n (n=1)`:** Handled perfectly. E.g., `["0"]` -> returns `"1"`. `["1"]` -> returns `"0"`.
*   **Largest `n (n=16)`:** The `O(N)` solution remains lightning fast, showcasing its efficiency over exponential `2^N` approaches.
*   **Problem Specifics:** The constraints `n == nums.length` (square matrix-like structure) and "return *any* answer" are crucial for the diagonal argument's direct applicability and simplicity.

**5. Key Patterns or Techniques Used:**
*   **Cantor's Diagonalization:** A powerful constructive proof/technique used to show existence of an element outside a set by systematically differing from each set member.
*   **Constructive vs. Search:** When "any valid answer" is allowed, always consider if a direct construction is possible, as it often leads to highly optimal solutions compared to exhaustive search.
*   **Leveraging Constraints:** The `N` strings of length `N` is the key structure that enables the elegant diagonal solution.
*   **"Small N" Hint:** While `N <= 16` might suggest `O(2^N)` solutions are acceptable, this problem highlights that an `O(N)` solution might exist and is vastly superior.