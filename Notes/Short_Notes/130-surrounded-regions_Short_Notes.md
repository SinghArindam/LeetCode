Here are concise short notes for quick revision of LeetCode problem 130: "Surrounded Regions".

---

### LeetCode 130: Surrounded Regions - Quick Revision Notes

#### 1. Key Problem Characteristics & Constraints
*   **Input:** `m x n` matrix `board` with characters `'X'` and `'O'`.
*   **Goal:** Capture (replace with `'X'`) all `'O'` regions that are "surrounded".
*   **"Surrounded" Definition:** An 'O' region is surrounded if:
    1.  It's fully enclosed by `'X'`s.
    2.  **Crucially:** *None* of its `'O'` cells are on the board's edge/border.
*   **Output:** Modify `board` **in-place**. No return value.
*   **Constraints:** `1 <= m, n <= 200`. Board cells are `'X'` or `'O'`.

#### 2. Core Algorithmic Approach (DFS/BFS - Optimal)
*   **Core Insight:** It's easier to find `'O'`s that are *NOT* surrounded than those that *ARE* surrounded. An `'O'` is not surrounded if it's connected to *any* `'O'` on the board's border.
*   **Steps:**
    1.  **Mark "Safe" 'O's:** Iterate through all cells on the **board's border**. If an `'O'` is found:
        *   Start a traversal (DFS or BFS) from this border `'O'`.
        *   During traversal, change all connected `'O'`s to a temporary marker (e.g., `'E'`, `'S'`, `'#'`). These are the "safe" `'O'`s that *should not be captured*.
    2.  **Final Conversion:** Iterate through the entire board again:
        *   If a cell is still an `'O'` (meaning it was not reachable from the border, hence surrounded), change it to `'X'`.
        *   If a cell is the temporary marker (e.g., `'E'`), change it back to `'O'` (restoring the safe regions).

#### 3. Important Time/Space Complexity Facts
*   Let `M` = rows, `N` = columns. Total cells = `M * N`.
*   **Time Complexity:** `O(M * N)`
    *   Each cell is visited/processed at most a constant number of times (once for border check, once for traversal if it's "safe", and once for final conversion).
*   **Space Complexity:** `O(M * N)` in the worst case.
    *   **DFS (recursive):** Recursion stack depth can be `M * N`.
    *   **BFS / Iterative DFS (with explicit stack):** Queue/stack can hold up to `M * N` elements.
    *   Board modification is in-place; temporary markers don't add auxiliary space.

#### 4. Critical Edge Cases to Remember
*   **Empty/Invalid Board:** `[]` or `[[]]`. Handled by an initial `if not board or not board[0]: return` check.
*   **1x1 Board:**
    *   `[["X"]]`: Remains `[["X"]]`.
    *   `[["O"]]`: Remains `[["O"]]` (it's on the border, thus not surrounded). Logic correctly marks it temporarily and restores.
*   **Board Full of 'X's:** No 'O's to process. Remains unchanged.
*   **Board Full of 'O's:** All 'O's are connected to the border. All will be marked temporarily and restored. Board remains unchanged. (No 'O's are surrounded).
*   **Constraints (M, N <= 200):** `O(M*N)` solution is highly efficient enough (max 40,000 cells).

#### 5. Key Patterns or Techniques Used
*   **Inverting the Problem / Complementary Logic:** A powerful strategy when directly identifying desired elements is hard; instead, identify what *doesn't* fit the criteria.
*   **Graph Traversal on Grids:** DFS (recursive or iterative with stack) or BFS (with queue) is standard for exploring connected components/reachability on 2D grids.
*   **Multi-Phase Processing:** Break down problem into distinct stages:
    1.  Initialization/Boundary Check
    2.  Traversal/Marking
    3.  Final Transformation
*   **Temporary Markers:** Using a temporary character (`'E'`, `'S'`, `'#'`) to mark visited/processed states in-place without needing a separate `visited` array.
*   **Union-Find (DSU):** An alternative, but more complex, approach for tracking connected components and their relation to a "safe" dummy node. Often overkill for static grid connectivity compared to DFS/BFS unless dynamic updates are involved.