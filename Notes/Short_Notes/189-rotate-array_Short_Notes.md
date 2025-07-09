Here are concise short notes for quick revision of LeetCode problem 189 - Rotate Array:

---

### **LeetCode 189: Rotate Array - Quick Revision Notes**

**1. Problem Characteristics & Constraints:**
*   **Goal:** Rotate integer array `nums` right by `k` steps.
*   **Crucial:** Must be done **in-place** (modify `nums` directly, `O(1)` extra space highly desired).
*   `k` is non-negative.
*   Array size `n`: `1 <= n <= 10^5`.
*   `k`: `0 <= k <= 10^5`.

**2. Core Algorithmic Approach (Optimal):**
*   **Three-Reversal Trick (Optimal `O(1)` Space):**
    1.  **Normalize `k`**: `k = k % n`. (Reduces `k` to effective rotations, handles `k > n` and `k = 0/n`).
    2.  **Reverse Entire Array**: `nums[0...n-1]`.
    3.  **Reverse First `k` Elements**: `nums[0...k-1]`.
    4.  **Reverse Remaining `n-k` Elements**: `nums[k...n-1]`.

*   **Pythonic Slicing (Common, but `O(N)` Space):**
    *   `k = k % n`
    *   `nums[:] = nums[-k:] + nums[:-k]`
    *   *Note:* Concatenation and slicing create temporary lists, making it `O(N)` space.

**3. Time/Space Complexity Facts:**
*   **Optimal (Reversal / Cyclic Replacements):**
    *   Time: `O(N)` (Each element visited/swapped a constant number of times).
    *   Space: `O(1)` (Truly in-place, no auxiliary data structure scaled with `N`).
*   **Python Slicing:**
    *   Time: `O(N)` (Slicing and concatenation).
    *   Space: `O(N)` (Temporary lists created for slices and concatenation).
*   Brute-Force (Repeated single shifts): `O(N*k)` time, `O(1)` space. (Too slow for large `N`, `k`).
*   Extra Array: `O(N)` time, `O(N)` space.

**4. Critical Edge Cases:**
*   **`k = 0` or `k` is a multiple of `n`**: Handled by `k = k % n` (effective `k` becomes 0, no rotation needed).
*   **`k > n`**: Handled by `k = k % n` (e.g., `k=10, n=7` becomes `k=3`).
*   **`n = 1` (single element array)**: Handled by `k = k % 1` (effective `k` becomes 0, array remains unchanged).
*   **`n = 0` (empty array)**: Not possible per constraints (`1 <= nums.length`).
*   **Negative `k`**: Not possible per constraints (`0 <= k`).

**5. Key Patterns / Techniques Used:**
*   **Modulo Arithmetic**: `k = k % n` is fundamental for cyclic operations to normalize `k`.
*   **In-place Reversal (`arr[start], arr[end] = arr[end], arr[start]`)**: A powerful and elegant pattern for `O(1)` space array rotations and other permutations. Decomposes complex operations into simpler reversals.
*   **Python `nums[:] = new_list`**: Modifies the *content* of the original list in-place (differs from `nums = new_list` which rebinds the variable).
*   **Problem Decomposition**: Breaking down a complex array manipulation into a series of simpler, well-understood transformations.