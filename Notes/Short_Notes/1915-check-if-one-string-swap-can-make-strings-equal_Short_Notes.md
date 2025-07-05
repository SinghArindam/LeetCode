Here are concise notes for quick revision of LeetCode problem 1915:

---

### LeetCode 1915: Check if One String Swap Can Make Strings Equal

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Make `s1` and `s2` equal.
*   **Operation:** **At most one** string swap (0 or 1 swap) on **exactly one** of the strings.
*   **Input:** Two strings `s1`, `s2` of equal length (`N`).
*   **Constraints:** `1 <= N <= 100`, lowercase English letters.

**2. Core Algorithmic Approach (Optimized):**
*   **Strategy:** Analyze the number and nature of differences between `s1` and `s2`.
*   **Steps:**
    1.  **Count differences:** Iterate through `s1` and `s2` simultaneously. Store indices or character pairs `(s1[i], s2[i])` where `s1[i] != s2[i]`.
    2.  **Case Analysis based on `diff_count` (number of mismatches):**
        *   **`diff_count == 0`**: Strings are already equal. Return `True` (0 swaps).
        *   **`diff_count == 1`**: Impossible. A single swap always affects two positions. Return `False`.
        *   **`diff_count == 2`**: Possible IF the two differing character pairs are "cross-matched".
            *   Let differences be at `idx1` and `idx2`.
            *   Condition: `s1[idx1] == s2[idx2]` AND `s1[idx2] == s2[idx1]`.
            *   (Equivalently: `diff_pair_1 == reverse(diff_pair_2)`).
            *   If true, return `True`. Else, return `False`.
        *   **`diff_count > 2`**: Impossible. A single swap can fix at most two positions. Return `False`.

**3. Important Time/Space Complexity Facts:**
*   **Time Complexity:** `O(N)`
    *   Single pass to find differences.
    *   Constant time operations for checks.
*   **Space Complexity:** `O(1)`
    *   The list/storage for differences stores at most 2 character pairs (for a `True` case).

**4. Critical Edge Cases to Remember:**
*   **Strings already equal:** `s1 = "kelb", s2 = "kelb"` (Returns `True`)
*   **Strings of length 1:**
    *   `s1 = "a", s2 = "a"` (Returns `True`)
    *   `s1 = "a", s2 = "b"` (Returns `False` - 1 diff)
*   **Exactly one difference:** `s1 = "abc", s2 = "abd"` (Returns `False`)
*   **Exactly two differences (valid swap):** `s1 = "bank", s2 = "kanb"` (Returns `True`)
    *   Diffs: `('b','k')` and `('k','b')`. `('b','k') == ('k','b')[::-1]` is true.
*   **Exactly two differences (invalid swap):** `s1 = "abcde", s2 = "axcye"` (Returns `False`)
    *   Diffs: `('b','x')` and `('d','y')`. `('b','x') == ('d','y')[::-1]` is false.
*   **More than two differences:** `s1 = "attack", s2 = "defend"` (Returns `False`)
    *   (Early exit optimization is key here).

**5. Key Patterns or Techniques Used:**
*   **Analyze Differences vs. Simulate Operations:** Focus on the state differences rather than brute-forcing operations.
*   **Case Analysis by Count:** Categorize problems based on the number of differing elements (0, 1, 2, >2).
*   **Symmetry/Cross-Matching for Swaps:** For single-swap problems, recognize the property `A[i]=B[j]` and `A[j]=B[i]`.
*   **Early Exit Optimization:** Return `False` as soon as impossibility is determined (e.g., `diff_count > 2`).
*   **Pythonic Conciseness:** `zip`, list comprehensions, `[::-1]` for tuple/list reversal.