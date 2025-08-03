Here are concise short notes for quick revision of LeetCode 3600: "Find the K-th Character in String Game I".

---

**LeetCode 3600: Find the K-th Character in String Game I**

**1. Key Problem Characteristics & Constraints:**
*   **Initial string:** `word = "a"`.
*   **Operation:** `word = word_original + transform(word_original)`
    *   `transform(char)`: `a->b, ..., y->z, z->a` (circular shift).
*   **String length doubles each operation:** `1, 2, 4, 8, ... , 2^N`.
*   **Goal:** Find the `k`-th character (1-indexed).
*   **Constraints:** `1 <= k <= 500`.

**2. Core Algorithmic Approach:**
*   **Optimized Recursive / Iterative Solution (Preferred):** Leverages the self-similar structure of the string generation.
*   **Logic:**
    *   **Base Case:** If `k = 1`, return `'a'`.
    *   **Recursive Step:**
        1.  Determine `midpoint`: The length of the first half of the string `S_N` (which is `S_{N-1}`).
            *   `midpoint = 1 << ((k - 1).bit_length() - 1)`
            *   This `midpoint` is the largest power of 2 less than `k`.
        2.  Since `k > midpoint` (for `k > 1`), the `k`-th character always falls into the *second half* (`transform(S_{N-1})`).
        3.  The character is found by transforming the character at position `k - midpoint` from the *previous* string generation.
        4.  Recursively call `kthCharacter(k - midpoint)` and then apply the `transform` function to its result.
*   **Character Transformation:** Simple `chr(ord(char) + 1)` or `if char == 'z': 'a'` logic.

**3. Important Time/Space Complexity Facts:**
*   **Optimal Solution (Recursive/Iterative):**
    *   **Time Complexity:** `O(log k)`. `k` is roughly halved in each step.
    *   **Space Complexity:** `O(log k)` for recursion stack (recursive), `O(1)` (iterative conversion).
*   **Naive Simulation:**
    *   **Time Complexity:** `O(k)`. String concatenation and iteration dominate.
    *   **Space Complexity:** `O(k)`. Stores the growing string.
    *   *(Note: `k <= 500` makes `O(k)` feasible, but `O(log k)` is theoretically more efficient and scalable for larger `k`.)*

**4. Critical Edge Cases to Remember:**
*   **`k = 1`:** Must be handled explicitly as the base case (`return 'a'`). This also avoids issues with `(0).bit_length()` in the `midpoint` calculation.
*   **`k` as a power of 2 (e.g., 2, 4, 8):** Correctly handled by the `midpoint` calculation and recursive logic, as `k` will always be `> midpoint`.

**5. Key Patterns or Techniques Used:**
*   **Self-Similarity / Recursion:** The problem has a clear recursive definition.
*   **Divide and Conquer:** The search space is halved in each step.
*   **Bit Manipulation:** Efficiently calculating powers of two (`1 << N`) and using `x.bit_length()` for finding the largest power of 2 less than `x`.
*   **Character Arithmetic:** `ord()` and `chr()` for simple alphabetical transformations.
*   **Iterative Conversion:** Recursive solutions can often be converted to iterative for constant space.