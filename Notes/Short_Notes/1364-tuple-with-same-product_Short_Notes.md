Here are concise short notes for quick revision of LeetCode problem 1364, "Tuple with Same Product":

---

### LeetCode 1364: Tuple with Same Product - Quick Revision Notes

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Find count of tuples `(a, b, c, d)` such that `a*b = c*d`.
*   **Conditions:** `a, b, c, d` must be **distinct** elements from `nums`.
*   **Input:** `nums` is an array of **distinct positive integers**.
*   **Constraints:**
    *   `1 <= nums.length <= 1000` (N)
    *   `1 <= nums[i] <= 10^4`

**2. Core Algorithmic Approach:**
*   **Transformation:** The condition `a*b = c*d` implies finding two *distinct pairs* `{a,b}` and `{c,d}` that yield the same product.
*   **Steps:**
    1.  **Generate Products:** Iterate through all unique pairs `(nums[i], nums[j])` where `i < j`.
    2.  **Count Product Frequencies:** Store the count of how many distinct pairs produce each unique product in a hash map (e.g., `defaultdict(int)`).
    3.  **Count Pair Combinations:** For each product `P` that appeared `k` times (meaning `k` distinct pairs have product `P`), calculate the number of ways to choose 2 of these pairs: `C(k, 2) = k * (k - 1) / 2`. Sum these up.
    4.  **Account for Tuple Permutations:** Each chosen combination of two distinct pairs (e.g., `{A,B}` and `{C,D}`) forms 8 distinct tuples:
        *   `2` ways for `(a,b)`: `(A,B)` or `(B,A)`
        *   `2` ways for `(c,d)`: `(C,D)` or `(D,C)`
        *   `2` ways to swap pair order: `(pair1, pair2)` or `(pair2, pair1)`
        *   Total = `2 * 2 * 2 = 8`.
    5.  **Final Result:** `(Sum of C(k, 2) for all products) * 8`.

**3. Important Time/Space Complexity Facts:**
*   **Time Complexity: `O(N^2)`**
    *   Outer loops to generate pairs: `O(N^2)`.
    *   Hash map operations: `O(1)` average.
    *   Iterating through hash map values: Max `O(N^2)` distinct products.
    *   `N=1000` means `10^6` operations, well within limits.
*   **Space Complexity: `O(N^2)`**
    *   Hash map stores product counts.
    *   Worst case: All `N*(N-1)/2` pairs produce distinct products.
    *   `1000^2 = 10^6` entries is manageable memory.

**4. Critical Edge Cases to Remember:**
*   **`nums.length < 4`**: Impossible to form 4 distinct elements. Solution correctly returns 0. (The `C(k, 2)` formula results in 0 if `k < 2`, and loops won't create enough distinct pairs for `k >= 2`).
*   **`nums` elements are distinct (Given)**: Crucial! This guarantees if two *different* pairs `{a,b}` and `{c,d}` have the same product, then `a,b,c,d` are automatically distinct. This validates the `* 8` factor directly.
*   **`nums` elements are positive (Given)**: Simplifies product handling (no zeros or negative product ambiguities).

**5. Key Patterns or Techniques Used:**
*   **Problem Transformation**: Converting a 4-variable problem into a 2-pair problem.
*   **Hashing/Frequency Counting**: Efficiently grouping and counting occurrences of derived values (products).
*   **Combinatorics**:
    *   `C(n, k)` (combinations formula) for selecting groups.
    *   Permutation counting for final tuple formation.
*   **Leveraging Constraints**: Using `N` limits to guide complexity expectations (`O(N^2)` is good), and properties of `nums` (distinct, positive) to simplify logic.
*   **Pairwise Iteration**: Standard nested loops `for i in range(n): for j in range(i+1, n):` for generating unique pairs.