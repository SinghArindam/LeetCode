Here are concise short notes for quick revision of LeetCode problem 733, Flood Fill:

---

### LeetCode 733: Flood Fill - Quick Revision Notes

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Change color of a connected component of pixels from a starting point `(sr, sc)` to a `new_color`.
*   **Connectivity:** Only 4-directional (up, down, left, right) adjacency is considered.
*   **Condition:** Pixels must have the *same original color* as `image[sr][sc]` to be part of the component.
*   **Constraints:** Grid size `1 <= m, n <= 50`. Pixel values up to `2^16-1`. `sr, sc` are valid indices.

**2. Core Algorithmic Approach:**
*   **Nature:** Classic **Graph Traversal** problem on a 2D grid. Grid cells are nodes, 4-directional adjacencies are edges.
*   **Methods:** Both **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** are optimal and commonly used.
    *   **DFS (Recursive Solution):**
        1.  Get `original_color = image[sr][sc]`.
        2.  Define a recursive helper function `dfs(r, c)`:
            *   **Base Cases:** If `(r, c)` is out of bounds OR `image[r][c] != original_color`, return.
            *   **Action:** Set `image[r][c] = new_color`.
            *   **Recurse:** Call `dfs` for all 4 neighbors.
        3.  Start with `dfs(sr, sc)`.
    *   **BFS (Iterative Solution):**
        1.  Get `original_color = image[sr][sc]`.
        2.  Initialize a queue with `(sr, sc)`.
        3.  While queue is not empty:
            *   Dequeue `(r, c)`.
            *   Set `image[r][c] = new_color`.
            *   For each of its 4 neighbors `(nr, nc)`:
                *   If `(nr, nc)` is in bounds AND `image[nr][nc] == original_color`, enqueue `(nr, nc)`.

**3. Important Time/Space Complexity Facts:**
*   Let `N = M * N` (total pixels).
*   **Time Complexity: O(N)** (or O(M * N)). Each pixel is visited and processed at most once.
*   **Space Complexity: O(N)** (or O(M * N)).
    *   **DFS:** For recursion stack depth in worst case (e.g., snake-like path).
    *   **BFS:** For queue size in worst case (e.g., entire grid is one component).
*   Both approaches are asymptotically optimal.

**4. Critical Edge Cases:**
*   **Starting pixel already has `new_color` (`image[sr][sc] == color`)**:
    *   **Handling:** **Crucial optimization**: `if image[sr][sc] == color: return image`. This prevents infinite loops/recursion if `original_color` is the same as `new_color`, and also avoids unnecessary traversal.
*   **1x1 image, starting pixel on boundary, entire image same color, only starting pixel is target color**: All are correctly handled by the general traversal logic and boundary/color checks.

**5. Key Patterns & Techniques Used:**
*   **Grid Traversal as Graph Traversal**: Common pattern to apply DFS/BFS on 2D arrays.
*   **Implicit Graph Representation**: The grid itself acts as the graph; no explicit adjacency lists needed.
*   **In-place "Visited" Marking**: Changing `image[r][c]` to `new_color` serves as marking it visited. Subsequent checks `image[r][c] != original_color` (DFS) or `image[r][c] == original_color` (BFS) correctly identify unvisited, eligible pixels.
*   **Boundary Checks**: Essential `0 <= r < rows` and `0 <= c < cols` to prevent `IndexError`.
*   **Direction Arrays**: Using `dr = [0,0,1,-1]` and `dc = [1,-1,0,0]` to easily iterate 4 neighbors.
*   **Early Exit Optimization**: Improve efficiency by handling trivial cases upfront (e.g., `start_color == new_color`).