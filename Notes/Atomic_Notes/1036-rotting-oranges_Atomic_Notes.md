Here's a set of atomic notes generated from the comprehensive and short notes for LeetCode problem 1036-rotting-oranges:

---

**Atomic Notes for LeetCode 1036: Rotting Oranges**

-   **Concept**: Problem Objective (Rotting Oranges)
    **Context**: Find the minimum minutes for all fresh oranges in a grid to become rotten.
    **Example**: Given grid `[[2,1,1],[1,1,0],[0,1,1]]`, determine minimum time.

-   **Concept**: Grid Cell Values
    **Context**: Representation of orange states in the grid.
    **Example**: `0` (empty cell), `1` (fresh orange), `2` (rotten orange).

-   **Concept**: Rotting Mechanism
    **Context**: How fresh oranges turn rotten.
    **Example**: Every minute, any fresh orange 4-directionally adjacent (up, down, left, right) to a rotten orange becomes rotten.

-   **Concept**: Impossible Scenario Handling
    **Context**: What to return if some fresh oranges can never rot.
    **Example**: If any fresh oranges remain after the process, return `-1`.

-   **Concept**: Optimal Algorithm Choice
    **Context**: Selecting the most suitable algorithm for minimum time on an unweighted grid.
    **Example**: Breadth-First Search (BFS) is optimal for "shortest path" or "minimum time" problems on unweighted graphs/grids.

-   **Concept**: Multi-Source BFS
    **Context**: Handling multiple initial sources for a spreading process.
    **Example**: Initialize the BFS queue with all initially rotten oranges (all cells with `2`) as starting points.

-   **Concept**: Level-by-Level Processing in BFS
    **Context**: Accurately counting minutes/steps in a BFS.
    **Example**: At the beginning of each minute's iteration, get `current_level_size = len(queue)`. Process exactly `current_level_size` elements before incrementing the `minutes` counter.

-   **Concept**: BFS Queue Initialization
    **Context**: Setting up the BFS queue before traversal begins.
    **Example**: Iterate through the grid, add coordinates `(r, c)` of all `grid[r][c] == 2` (rotten oranges) to the queue.

-   **Concept**: Counting Fresh Oranges
    **Context**: Tracking the progress of rotting and determining impossibility.
    **Example**: Maintain a `fresh_oranges_count`. Decrement it each time a fresh orange turns rotten.

-   **Concept**: Handling "No Fresh Oranges Initially" Edge Case
    **Context**: A specific scenario where no time is needed.
    **Example**: If `fresh_oranges_count == 0` at the very start, return `0` minutes.

-   **Concept**: Grid Boundary Check
    **Context**: Ensuring neighbor coordinates are valid during traversal.
    **Example**: When checking `(nr, nc)` for a neighbor, verify `0 <= nr < R` and `0 <= nc < C`.

-   **Concept**: In-Place Grid Modification
    **Context**: Marking processed/visited cells in a grid-based BFS.
    **Example**: When a fresh orange `grid[nr][nc] == 1` rots, change its value to `2` to mark it as rotten and visited.

-   **Concept**: Enqueuing Newly Rotten Oranges
    **Context**: Propagating the rotting process to the next minute's layer.
    **Example**: After `grid[nr][nc]` changes from `1` to `2`, add `(nr, nc)` to the BFS queue. These will act as sources for the next minute.

-   **Concept**: Final Check for Unreachable Oranges
    **Context**: Determining if the rotting process was incomplete.
    **Example**: After the BFS loop finishes, if `fresh_oranges_count > 0`, return `-1`.

-   **Concept**: Time Complexity of BFS (Rotting Oranges)
    **Context**: Efficiency of the optimal BFS solution.
    **Example**: O(R * C), where R is rows and C is columns, because each cell is visited and processed at most a constant number of times.

-   **Concept**: Space Complexity of BFS (Rotting Oranges)
    **Context**: Memory usage of the optimal BFS solution.
    **Example**: O(R * C) in the worst case, as the queue might hold up to all grid coordinates (e.g., checkerboard pattern of oranges).

-   **Concept**: Direction Arrays
    **Context**: A common technique for iterating through 4-directional or 8-directional neighbors.
    **Example**: Use `directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]` to easily calculate `(r + dr, c + dc)`.

-   **Concept**: Efficient Queue Data Structure
    **Context**: Choosing the right data structure for BFS queue operations.
    **Example**: Use `collections.deque` in Python for O(1) `append()` and `popleft()` operations, more efficient than `list.pop(0)`.

-   **Concept**: Handling "No Rotten Oranges Initially" Edge Case
    **Context**: Scenario where no spreading can begin.
    **Example**: If `ls_rotten` (queue) is empty at the start and `num_of_fresh > 0`, the BFS loop will not run. The final check `if num_of_fresh > 0` correctly returns `-1`.

-   **Concept**: Iterative Grid Simulation (Alternative Approach)
    **Context**: A less efficient but intuitive simulation approach.
    **Example**: Scan the entire `M x N` grid in each minute to identify oranges that spread, leading to O(M*N*(M+N)) time complexity.

-   **Concept**: DFS for Shortest Path (Critique)
    **Context**: Why standard DFS is generally not preferred for shortest path on unweighted graphs.
    **Example**: DFS explores depth-first, potentially finding longer paths first; adapting it to track minimum time often makes it less efficient or more complex than BFS.