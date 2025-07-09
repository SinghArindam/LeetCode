Here are concise short notes for LeetCode problem 169 - Majority Element, suitable for quick revision:

---

### LeetCode 169: Majority Element - Quick Revision Notes

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Find the element that appears `> ⌊n / 2⌋` times.
*   **Critical Guarantee:** The majority element **always exists** in the array.
*   **Constraints:** `1 <= n <= 5 * 10^4`, `-10^9 <= nums[i] <= 10^9`.
*   **Follow-up:** Solve in O(N) time and O(1) space.

**2. Core Algorithmic Approach (Optimal):**
*   **Boyer-Moore Voting Algorithm:**
    *   Initialize `candidate = None`, `count = 0`.
    *   Iterate through `num` in `nums`:
        *   If `count == 0`: set `candidate = num`, `count = 1`.
        *   Else if `num == candidate`: `count++`.
        *   Else (`num != candidate`): `count--`.
    *   Return `candidate`.
    *   **Logic:** Acts like a "cancellation" process. Each non-majority element cancels one instance of the current candidate. Since the majority element appears `> n/2` times, its net count will always be positive, making it the final `candidate`.

**3. Important Time/Space Complexity Facts:**
*   **Boyer-Moore (Optimal):**
    *   Time: **O(N)** (single pass).
    *   Space: **O(1)** (constant extra variables).
*   **Other Common Approaches:**
    *   **Sorting:** Time O(N log N), Space O(N) (for typical built-in sort). Element at `nums[n//2]` is the majority.
    *   **Hash Map:** Time O(N), Space O(N) (to store frequencies).

**4. Critical Edge Cases & Considerations:**
*   **`n = 1`:** Algorithm works correctly (e.g., `[7]` returns `7`).
*   **All elements are the same:** Handled correctly.
*   **Crucial Guarantee:** "Majority element always exists" simplifies Boyer-Moore; **no second pass for verification is needed**. The found candidate is guaranteed to be the majority.

**5. Key Patterns or Techniques Used:**
*   **Boyer-Moore Voting Algorithm:** Specialized for finding elements with `> N/2` frequency (or `> N/k` with adaptations). Relies on a "cancellation" principle.
*   **Frequency Counting:** General technique using Hash Maps for counting occurrences.
*   **Leveraging Sorted Properties:** Recognizing that sorting can reveal positional properties (e.g., majority element at the median index).