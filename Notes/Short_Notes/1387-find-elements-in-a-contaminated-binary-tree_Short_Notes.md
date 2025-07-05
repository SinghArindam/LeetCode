Here are concise short notes for quick revision of LeetCode Problem 1387:

---

## LeetCode 1387: Find Elements in a Contaminated Binary Tree - Quick Notes

### 1. Key Problem Characteristics & Constraints:

*   **Goal:** Implement `FindElements` class to:
    1.  **Recover** a contaminated binary tree (all `node.val = -1`).
    2.  Efficiently `find(target)` if a value exists in the recovered tree.
*   **Recovery Rules:**
    *   `root.val = 0`
    *   `left.val = 2 * parent.val + 1`
    *   `right.val = 2 * parent.val + 2`
*   **Constraints:**
    *   Tree `height <= 20` (limits recursion depth, max N roughly 2M, but N is lower).
    *   Total nodes `N = [1, 10^4]`.
    *   Total `find()` calls `Q = [1, 10^4]`.
    *   `target` value `[0, 10^6]` (fits `int`, values are non-negative).
    *   **Crucial:** Generated values are unique.

### 2. Core Algorithmic Approach:

*   **Strategy:** **Pre-computation** during `FindElements` constructor.
    *   Avoids redundant calculations for repeated `find` calls.
*   **Recovery (`FindElements` constructor):**
    *   Perform a **Depth-First Search (DFS)** traversal starting from `root` (initial value `0`).
    *   For each visited node, calculate its correct value based on its parent's value and the rules.
    *   Store **all** calculated (recovered) node values in a **hash set** (`std::unordered_set<int>`).
*   **Finding (`find(target)` method):**
    *   Simply check if the `target` value exists in the pre-computed hash set.

### 3. Important Time/Space Complexity Facts:

*   **Constructor (`FindElements(TreeNode* root)`):**
    *   **Time:** O(N) – Each node visited once for DFS, hash set insertion is O(1) average.
    *   **Space:** O(N) for storing all `N` unique values in the `unordered_set`. O(H) for recursion stack (where H <= 20, negligible compared to N).
*   **`find(int target)`:**
    *   **Time:** O(1) on average – Hash set lookup.
    *   **Space:** O(1).
*   **Overall Efficiency:** O(N + Q) – Highly efficient for the given constraints (10^4 + 10^4 operations).

### 4. Critical Edge Cases:

*   **Empty Tree:** Problem constraint `N >= 1` means `root` is never `nullptr`.
*   **Single Node Tree:** Constructor correctly adds `0` to the set. `find(0)` works.
*   **Skewed Trees:** Handled correctly by DFS. Height constraint (20) prevents stack overflow.
*   **Value Range:** `int` is sufficient for node values and `target` values.
*   **Duplicate Values:** Not an issue; the `2x+1`, `2x+2` rules guarantee all generated values in the tree are unique.

### 5. Key Patterns & Techniques Used:

*   **Pre-computation / Memoization:** Store results of expensive initial setup for fast subsequent queries.
*   **Tree Traversal (DFS/BFS):** Standard for processing all nodes in a tree. DFS (recursive) is natural for passing parent-dependent state.
*   **Hash Set (`std::unordered_set`):** The go-to data structure for fast average O(1) existence checks (`.count()` or `.find()`).
*   **State Passing in Recursion:** Passing the `current_val` to children to compute their values.
*   **Constraint Analysis:** Constraints (N, Q, H) are critical indicators for choosing optimal `O(N + Q)` solution over `O(N*Q)`.