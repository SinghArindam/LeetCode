Here are concise short notes for quick revision of LeetCode problem 1036 - Rotting Oranges:

---

### LeetCode 1036: Rotting Oranges - Quick Revision Notes

#### 1. Key Problem Characteristics & Constraints
*   **Grid Values:** `0` (empty), `1` (fresh orange), `2` (rotten orange).
*   **Rotting Rule:** Fresh oranges become rotten if 4-directionally adjacent to a rotten orange. Happens every minute.
*   **Goal:** Minimum minutes for all fresh oranges to rot. Return `-1` if impossible.
*   **Constraints:** Grid size `m, n` up to `10x10`. Small grid.

#### 2. Core Algorithmic Approach (BFS)
*   **Strategy:** Multi-Source Breadth-First Search (BFS).
*   **Why BFS?** Problem asks for minimum time/steps on an unweighted grid, which is a classic BFS application.
*   **Steps:**
    1.  **Initialization:**
        *   Find all initial rotten oranges (`2`) and add their coordinates to a queue (e.g., `collections.deque`).
        *   Count total `fresh_oranges_count` (`1`s).
        *   Initialize `minutes = 0`.
    2.  **Edge Case 1:** If `fresh_oranges_count == 0` initially, return `0`.
    3.  **BFS Loop (Minute by Minute):**
        *   While queue is not empty AND `fresh_oranges_count > 0`:
            *   Get `current_level_size = len(queue)` to process oranges rotting in *this* minute.
            *   For `_` in `current_level_size`:
                *   Dequeue `(r, c)`.
                *   For each 4-directional neighbor `(nr, nc)`:
                    *   If `(nr, nc)` is in bounds and `grid[nr][nc] == 1` (fresh):
                        *   Change `grid[nr][nc]` to `2` (rotten).
                        *   Decrement `fresh_oranges_count`.
                        *   Enqueue `(nr, nc)` (these will spread in the *next* minute).
            *   Increment `minutes` after processing a full layer.
    4.  **Final Check:**
        *   If `fresh_oranges_count > 0` after loop, return `-1` (some fresh oranges unreachable).
        *   Else, return `minutes`.

#### 3. Important Time/Space Complexity
*   **Time Complexity:** `O(R * C)` where `R` is rows, `C` is columns. Each cell is visited and processed a constant number of times.
*   **Space Complexity:** `O(R * C)` in the worst case, due to the queue storing up to all cells. Grid is modified in-place.

#### 4. Critical Edge Cases to Remember
*   **No Fresh Oranges at Start:** `[[0,2]]` or `[[0,0]]` -> Output `0`. Handled by initial `fresh_oranges_count == 0` check.
*   **No Rotten Oranges at Start (but fresh exist):** `[[1,1]]` -> Output `-1`. Handled by `fresh_oranges_count > 0` after BFS loop completes (queue empty).
*   **Unreachable Fresh Oranges:** `[[2,1,1],[0,1,1],[1,0,1]]` -> Output `-1`. Handled by final `fresh_oranges_count > 0` check.
*   **Single Cell Grid:** `[[0]]`, `[[1]]`, `[[2]]` are all handled correctly by the general logic.

#### 5. Key Patterns or Techniques
*   **BFS for Shortest Path:** Go-to for minimum steps/time on unweighted graphs/grids.
*   **Multi-Source BFS:** Queue initialized with all starting points.
*   **Level-by-Level Processing:** Essential for correctly counting "minutes" (layers). Achieved by getting queue size at start of each minute's iteration.
*   **In-Place Grid Modification:** Changing `1` to `2` marks cells as visited/processed.
*   **Counter for Remaining Targets:** `fresh_oranges_count` allows efficient check for impossibility.
*   **Direction Arrays:** Simplifies neighbor iteration (e.g., `[(1,0), (-1,0), (0,1), (0,-1)]`).
*   **`collections.deque`:** Use for efficient queue operations (`append` and `popleft`).