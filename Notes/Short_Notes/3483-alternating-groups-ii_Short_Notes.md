Here are concise short notes for quick revision of LeetCode problem 3483: Alternating Groups II:

---

### **LeetCode 3483: Alternating Groups II - Quick Revision Notes**

1.  **Key Problem Characteristics & Constraints:**
    *   **Goal:** Count `k`-length "alternating groups" in a `colors` array (0=red, 1=blue).
    *   **Alternating:** `colors[i] != colors[i+1]` for all adjacent pairs within the `k`-group.
    *   **Circular Array:** `colors[N-1]` is adjacent to `colors[0]`.
    *   **Constraints:** `3 <= N <= 10^5`, `3 <= k <= N`.

2.  **Core Algorithmic Approach:**
    *   **Transformation:** Create `diff` array where `diff[i] = 1` if `colors[i] != colors[(i+1)%N]` (alternating transition), else `0`.
        *   An alternating group of `k` tiles implies `k-1` alternating transitions.
        *   So, a valid group corresponds to a window of `k-1` `1`s in `diff` (i.e., sum of `k-1` elements is `k-1`).
    *   **Circularity Handling:** To simplify sliding window, duplicate `diff` array to `ext` array of size `2N` (i.e., `ext = diff + diff`). This allows linear sliding.
    *   **Sliding Window:**
        1.  Initialize `current_sum` for the first `k-1` elements of `ext`.
        2.  Check if `current_sum == k-1`; if so, increment count.
        3.  Slide window `N-1` times: subtract element leaving window, add element entering window.
        4.  For each slide, if `current_sum == k-1`, increment count.

3.  **Important Time/Space Complexity Facts:**
    *   **Time Complexity: O(N)**
        *   Dominated by creating `diff` array, creating `ext` array, and the single pass of the sliding window.
    *   **Space Complexity: O(N)**
        *   Required for `diff` array (size `N`) and `ext` array (size `2N`).

4.  **Critical Edge Cases to Remember:**
    *   **`k=3` (minimum `k`):** `windowSize` is `2`. Algorithm correctly checks for 2 consecutive `1`s.
    *   **`k=N` (maximum `k`):** `windowSize` is `N-1`. If the entire circle is alternating, all `N` possible groups will be counted.
    *   **No alternating groups possible:** `diff` array won't have `k-1` consecutive `1`s; `current_sum` will never reach `k-1`. Returns `0`.
    *   **All same colors:** `diff` array will be all `0`s. Correctly returns `0`.
    *   The use of `(i+1)%N` for `diff` creation and array doubling for `ext` robustly handles circularity.

5.  **Key Patterns or Techniques Used:**
    *   **Problem Transformation:** Convert a boolean property (`alternating`) into numerical values (`0` or `1`) to facilitate summation.
    *   **Sliding Window:** Efficiently process fixed-length contiguous segments. Avoids recalculation.
    *   **Circular Array Handling:**
        *   Modulo operator (`% N`) for direct circular indexing.
        *   **Array Doubling/Extension (e.g., `2N` size):** A common, powerful technique to transform a circular sliding window problem into a linear one, simplifying logic.
    *   **Sum/Count Check:** Using the sum of `0/1` values in a window to verify a complex condition (e.g., all `k-1` transitions are alternating).