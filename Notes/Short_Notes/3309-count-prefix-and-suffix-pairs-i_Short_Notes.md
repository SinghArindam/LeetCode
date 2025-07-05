Here are concise short notes for quick revision of LeetCode problem 3309: "Count Prefix and Suffix Pairs I".

---

### LeetCode 3309: Count Prefix and Suffix Pairs I

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Count pairs `(i, j)` in `words` array where `i < j` and `words[i]` is both a prefix AND a suffix of `words[j]`.
*   **Input:** `words` (vector of strings).
*   **Constraints:**
    *   `N = words.length`: `1 <= N <= 50`
    *   `L = words[i].length`: `1 <= L <= 10`
    *   `words[i]` contains lowercase English letters.
*   **Definition:** `isPrefixAndSuffix(str1, str2)` is true if `str1` is prefix of `str2` AND `str1` is suffix of `str2`.

**2. Core Algorithmic Approach:**
*   **Brute-Force (Optimal for constraints):**
    *   Iterate through all possible pairs `(words[i], words[j])` such that `i < j`.
    *   For each pair, directly apply the `isPrefixAndSuffix` check.
*   **`isPrefixAndSuffix(str1, str2)` Logic:**
    1.  `str1.length() <= str2.length()`: `str1` cannot be longer than `str2`.
    2.  `str2.substr(0, str1.length()) == str1`: Checks prefix.
    3.  `str2.substr(str2.length() - str1.length()) == str1`: Checks suffix.
    4.  All three conditions must be true. (C++20 `starts_with` and `ends_with` handle #1 implicitly).

**3. Time/Space Complexity Facts:**
*   **Time Complexity: `O(N^2 * L)`**
    *   `N` (number of words) nested loops `O(N^2)` pairs.
    *   Each pair comparison involves string operations (`substr`, `==`) taking `O(L)` time.
    *   For `N=50, L=10`, `50^2 * 10 = 25,000` operations – extremely fast.
*   **Space Complexity: `O(L)`**
    *   For temporary string copies created by `substr` or for storing `str1`, `str2`.

**4. Critical Edge Cases:**
*   **`words.length = 1`:** Correctly returns `0` (no `i < j` pairs possible). Loop bounds handle this.
*   **`str1.length() > str2.length()`:** `isPrefixAndSuffix` immediately returns `false`. Handled by initial length check (`str1.length() <= str2.length()`).
*   **`str1 == str2`:** (e.g., `isPrefixAndSuffix("a", "a")`) Correctly returns `true`. A string is a prefix and suffix of itself.
*   **`words[i].length = 1`:** Smallest string length handled correctly. (e.g., `"a"` prefix/suffix of `"aba"`).
*   **No empty strings:** Problem constraint `words[i].length >= 1`.

**5. Key Patterns or Techniques Used:**
*   **Leveraging Constraints:** Small constraints (`N=50, L=10`) are the primary hint for a straightforward brute-force solution. Avoids over-optimization.
*   **Iterating `(i, j)` pairs with `i < j`:** Standard nested loop pattern:
    ```cpp
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            // ... check (words[i], words[j])
        }
    }
    ```
*   **String Manipulation:** Direct use of `substr()` for prefix and suffix checks, or modern C++20 `starts_with()`/`ends_with()`.
*   **Problem Decomposition:** Extracting the `isPrefixAndSuffix` logic into a helper function for clarity.