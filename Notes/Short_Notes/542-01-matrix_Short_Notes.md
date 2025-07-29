Here are concise short notes for LeetCode problem 542 - 01 Matrix, suitable for quick revision:

---

### LeetCode 542: 01 Matrix - Quick Revision Notes

**1. Key Problem Characteristics & Constraints:**
*   **Input:** `m x n` binary matrix (`mat`) with `0`s and `1`s.
*   **Output:** Transformed matrix where each cell `(r, c)` stores the *shortest distance* to its *nearest `0`*.
*   **Distance:** Manhattan distance (horizontal/vertical moves only, cost `1` per step).
*   **Guarantee:** At least one `0` exists in the matrix.
*   **Constraints:** `1 <= m, n <= 10^4`, `1 <= m * n <= 10^4`. (Implies total cells up to 10,000).

**2. Core Algorithmic Approach (Multi-Source BFS):**
*   **Strategy:** Instead of running BFS from each `1` (too slow, `O((MN)^2)`), initiate a single BFS simultaneously from *all* `0` cells.
*   **Initialization:**
    *   Add all cells with `0` to a `deque` (queue). Their distance is `0`.
    *   For cells with `1`, mark them as `-1` (or `infinity`) to signify "unvisited" or "distance unknown".
*   **BFS Traversal:**
    *   While the queue is not empty:
        *   Dequeue a cell `(r, c)`. `mat[r][c]` already holds its minimum distance.
        *   Explore its 4 neighbors `(nr, nc)` (up, down, left, right).
        *   If `(nr, nc)` is in bounds AND `mat[nr][nc]` is `-1` (unvisited `1`):
            *   Set `mat[nr][nc] = mat[r][c] + 1` (distance is one more than current cell).
            *   Enqueue `(nr, nc)` for further exploration.
*   **Why it works:** BFS explores layer by layer, guaranteeing that the first time a `1` cell is reached, it's via the shortest path from *any* initial `0`.

**3. Time/Space Complexity Facts:**
*   **Time Complexity:** `O(M * N)`
    *   Each cell is enqueued and dequeued at most once. Constant work for neighbors.
*   **Space Complexity:** `O(M * N)`
    *   For the `queue` in the worst case (e.g., entire matrix needs processing).
    *   Input matrix is modified in-place, so no additional output matrix space.
*   **Naive BFS (from each '1'):** `O((M*N)^2)` time - too slow.
*   **Dynamic Programming Alternative:** Also `O(M*N)` time and space (requires two passes).

**4. Critical Edge Cases:**
*   **Single cell:** `mat = [[0]]` -> `[[0]]`.
*   **All zeros:** `mat = [[0,0],[0,0]]` -> `[[0,0],[0,0]]`.
*   **Single zero surrounded by ones:** `[[1,1,1],[1,0,1],[1,1,1]]` -> `[[2,1,2],[1,0,1],[2,1,2]]`.
*   `M*N` constraint (`<= 10^4`) confirms `O(M*N)` solution is efficient enough.

**5. Key Patterns/Techniques Used:**
*   **Multi-Source BFS:** The primary pattern for "distance from nearest X" problems on unweighted grids.
*   **BFS for Shortest Paths:** Fundamental for unweighted graphs.
*   **Grid Traversal:** Using `directions` array `[(1,0), (-1,0), (0,1), (0,-1)]` for 4-way movement.
*   **In-Place Modification:** Reusing the input matrix (`mat[r][c] = -1`) to mark unvisited cells and store results, optimizing space.
*   **Dynamic Programming (DP):** An alternative (`O(M*N)`) approach for grid distance, often involves two passes (e.g., top-left to bottom-right, then bottom-right to top-left) to capture all neighbor dependencies.