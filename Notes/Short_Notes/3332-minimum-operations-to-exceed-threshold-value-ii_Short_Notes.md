Here are concise notes for quick revision of LeetCode problem 3332: "Minimum Operations to Exceed Threshold Value II".

---

### LeetCode 3332: Minimum Operations to Exceed Threshold Value II

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Minimum operations to make ALL array elements `&ge; k`.
*   **Operation:**
    1.  Take two smallest `x, y` from `nums`.
    2.  Remove `x, y`.
    3.  Add `min(x,y) * 2 + max(x,y)` back. (Effectively `2*x + y` if `x` is smallest).
*   **Constraints:**
    *   `nums.length`: `2` to `2 * 10^5`.
    *   `nums[i], k`: `1` to `10^9`.
    *   Operation needs `nums.size() &ge; 2`.
    *   **Crucial:** An answer *always exists*.

**2. Core Algorithmic Approach:**
*   **Greedy Strategy:** Always combine the two smallest elements. This is optimal because:
    *   It directly addresses the elements furthest below `k`.
    *   The new value (`2x+y`) is always greater than `x` and `y` (for `x &ge; 1`), ensuring progress.
    *   No other combination yields a faster path to success.
*   **Data Structure:** **Min-Priority Queue (Min-Heap)**. Ideal for efficiently retrieving and removing the smallest elements from a dynamic collection.
*   **Steps:**
    1.  Initialize `operations = 0`.
    2.  Insert all `nums` elements into a min-heap.
    3.  **Loop:** While `heap.top() < k`:
        *   Pop `x` (smallest) and `y` (second smallest).
        *   Calculate `newVal = 2 * x + y`.
        *   Push `newVal` back to heap.
        *   Increment `operations`.
    4.  Return `operations`.

**3. Time & Space Complexity:**
*   **Time: `O(N log N)`**
    *   `N` initial insertions: `N * O(log N)`.
    *   Up to `N-1` operations: Each involves 2 pops, 1 push (all `O(log N)`). Total `(N-1) * O(log N)`.
*   **Space: `O(N)`**
    *   For storing elements in the priority queue.

**4. Critical Edge Cases & Handling:**
*   **All elements initially `&ge; k`:**
    *   **Handling:** Loop condition `pq.top() < k` is immediately false. Returns `0` operations (correct).
*   **Only one element left in heap, and it's `< k`:**
    *   **Handling:** `if (pq.size() < 2)` check within loop (returns -1). However, problem guarantees answer exists, so this state *should not be reached* in valid test cases. It's a defensive check.
*   **Integer Overflow:** `nums[i], k` up to `10^9`. `2 * 10^9 + 10^9 = 3 * 10^9`, which exceeds standard 32-bit integer max (`~2.1 * 10^9`).
    *   **Handling:** Use `long long` for heap elements and all calculations (`x, y, newVal`).

**5. Key Patterns / Techniques:**
*   **Greedy Algorithms:** When problems involve iterative choices aiming for an optimum, especially with "extreme" elements.
*   **Priority Queues:** The go-to data structure for efficiently managing minimum/maximum elements in a mutable collection. Use `std::greater` for min-heap.
*   **Data Type Selection:** Always check constraints for potential integer overflow, use wider types (`long long` in C++) when calculations can exceed limits.
*   **Problem Simplification by Rules:** The explicit "take the two smallest" rule is a strong hint for the greedy approach, removing complex decision-making.
*   **Huffman Coding Analogy:** Similar pattern of repeatedly combining smallest elements to achieve a goal.