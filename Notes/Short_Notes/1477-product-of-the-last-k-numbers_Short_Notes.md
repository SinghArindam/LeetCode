Here are concise short notes for quick revision of LeetCode Problem 1477:

---

### LeetCode 1477: Product of the Last K Numbers - Quick Revision Notes

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Implement `ProductOfNumbers` class. `add(num)` appends to stream, `getProduct(k)` returns product of last `k` numbers.
*   **Constraints:**
    *   `0 <= num <= 100` (Crucial: `0` can appear).
    *   `getProduct(k)` always called when stream has at least `k` numbers.
    *   Product *guaranteed* to fit in a 32-bit integer (no overflow worries).
    *   Target: `O(1)` for both `add` and `getProduct`.

**2. Core Algorithmic Approach (Optimized): Prefix Products**
*   **Data Structure:** Use a `std::vector<int> prefixProducts`.
*   `prefixProducts[i]` stores the cumulative product of numbers *since the last `0` was added* (or since initialization).
*   **Initialization:** `prefixProducts` starts with `[1]`.
*   **`add(int num)`:**
    *   **If `num == 0`:** Reset `prefixProducts = {1}`. (Zero "clears" past products, any product including it is 0).
    *   **If `num != 0`:** Append `prefixProducts.back() * num` to `prefixProducts`.
*   **`getProduct(int k)`:**
    *   Let `n = prefixProducts.size()`.
    *   **Zero Check:** If `k >= n`, return `0`. (This means the `k` window includes a `0` that caused a reset).
    *   **Calculation:** Return `prefixProducts[n - 1] / prefixProducts[n - k - 1]`.
        *   `prefixProducts[n - 1]` is total product of current non-zero segment.
        *   `prefixProducts[n - k - 1]` is product of elements *before* the last `k` in this segment.

**3. Time & Space Complexity:**
*   **Time:**
    *   `ProductOfNumbers()`: O(1)
    *   `add(num)`: O(1) amortized (vector `push_back` and fixed-size reset).
    *   `getProduct(k)`: O(1) (constant array access and division).
*   **Space:** O(N), where N is the maximum number of non-zero elements stored between `0` resets (worst case: no zeros, so O(TotalAdds)).

**4. Critical Edge Cases & Handling:**
*   **Adding `0`:** Explicitly handled by resetting `prefixProducts` to `[1]`. This correctly invalidates previous products for any `k` window that would include this `0`.
*   **`getProduct(k)` spanning a past `0`:** Handled by the `if (k >= n) return 0;` condition in `getProduct`. If `k` is larger than the current non-zero segment length, it implies a `0` must have been involved.
*   **Initial state / Small `k`:** The `prefixProducts` initialized with `1` (`prefixProducts[0] = 1`) acts as a multiplicative identity and ensures correct division even when `k` represents the entire current non-zero segment (i.e., `prefixProducts[n - k - 1]` accesses `prefixProducts[0]`).
*   **Integer Overflow:** Problem explicitly guarantees products fit in 32-bit integers, so standard `int` is sufficient.

**5. Key Patterns / Techniques Used:**
*   **Prefix Products/Sums:** Fundamental technique for efficient range queries.
*   **Zero Handling:** Special strategy for product problems where `0`s break the division-based prefix product property. Resetting is an effective approach here.
*   **Sentinel/Identity Element:** Using `1` at the beginning of `prefixProducts` simplifies index calculations and base cases for division.
*   **Dynamic Array (`std::vector`):** Efficiently stores a growing sequence of numbers/products for stream processing.