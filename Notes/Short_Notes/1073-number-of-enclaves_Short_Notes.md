Here's a concise summary of LeetCode Problem 1073 (Number of Enclaves) suitable for quick revision:

---

### LeetCode 1073: Number of Enclaves (Short Notes)

**1. Problem Characteristics & Constraints:**
*   **Goal:** Count `land cells (1s)` from which you **cannot** reach the grid boundary (0, 4-directionally).
*   **Input:** `m x n` binary matrix (`0` = sea, `1` = land).
*   **Movement:** 4-directional adjacency between land cells.
*   **Constraints:** `1 <= m, n <= 500`. Grid cells are `0` or `1`.

**2. Core Algorithmic Approach (Flood Fill from Borders - DFS/BFS):**
*   **Core Idea:** Any land cell that *can* walk off the boundary must be part of a connected component that touches the boundary.
*   **Strategy:**
    1.  **Identify & "Sink" Border-Reachable Land:** Iterate through all cells on the grid's perimeter (rows 0 & `m-1`, columns 0 & `n-1`).
    2.  If a border cell is `1` (land), start a **DFS (or BFS)** traversal from it.
    3.  During traversal, change all connected `1`s to `0` (or `2`, or mark as `visited`) in-place. This marks them as "sunk" or "reachable from boundary".
    4.  **Count Remaining Enclaves:** After all border-connected land cells are "sunk," iterate through the entire grid and sum up the remaining `1`s. These are the truly enclaved land cells.

**3. Time & Space Complexity:**
*   **Time Complexity:** `O(M * N)`
    *   Each cell is visited a constant number of times (initial border check, DFS/BFS traversal if applicable, final summation).
*   **Space Complexity:** `O(M * N)`
    *   Due to the recursion stack depth (for DFS) or queue size (for BFS) in the worst case (e.g., a grid full of `1`s forming a snake-like path).

**4. Critical Edge Cases:**
*   **Empty/Single-dimension Grid:** Handled by `len(grid)` and `len(grid[0])` checks; result `0`.
*   **Grid with All `0`s (Sea):** No land cells, count `0`.
*   **Grid with All `1`s (Land):** All land is boundary-reachable, count `0`.
*   **Grid with 1 Row/Column:** All `1`s are boundary-reachable, count `0`.
*   **Isolated Enclave:** E.g., `[[0,0,0],[0,1,0],[0,0,0]]` - `1` in center is correctly counted.
*   **Disconnected Components:** Only boundary-connected components are "sunk"; others remain and are counted.

**5. Key Patterns / Techniques:**
*   **Graph Traversal on Grids:** DFS/BFS are fundamental for connected components.
*   **Flood Fill:** A classic application where connected regions are identified and processed.
*   **Inverse Logic (Complementary Counting):** Often easier to find elements that *do* satisfy a condition (reachable from boundary) and exclude them, rather than directly finding elements that *don't*.
*   **In-place Grid Modification:** Efficiently marks visited cells without extra space for a `visited` set (though a separate `visited` set is also a valid alternative).
*   **Boundary Conditions:** Special attention to `row=0, m-1` and `col=0, n-1` is crucial for starting traversals.
*   **Recursion Depth:** Be aware of Python's recursion limit for very large grids; BFS is safer in such cases.