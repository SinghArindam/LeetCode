Here is a set of atomic notes for LeetCode problem 542-01-matrix, suitable for spaced repetition learning:

---

-   **Concept**: Problem Goal - Shortest Distance to Nearest Zero.
    **Context**: For each cell `(r, c)` in a binary matrix, compute the minimum steps to reach any cell containing `0`.
    **Example**: Input `[[0,1,0]]` yields `[[0,1,0]]`. Input `[[1,1,1],[1,0,1],[1,1,1]]` yields `[[2,1,2],[1,0,1],[2,1,2]]`.

-   **Concept**: Distance Definition (Manhattan Distance).
    **Context**: The distance is defined as the number of steps moving horizontally or vertically to an adjacent cell (sharing a common edge), with each step costing `1`. Diagonal moves are not allowed.
    **Example**: From `(r,c)`, possible moves are `(r+1,c), (r-1,c), (r,c+1), (r,c-1)`.

-   **Concept**: Problem Constraint - At Least One Zero.
    **Context**: The input matrix `mat` is guaranteed to contain at least one `0`. This ensures that every `1` cell has a valid nearest `0` to which a distance can be calculated.

-   **Concept**: Naive Approach - BFS/DFS from Each '1' Cell.
    **Context**: A less efficient method where a separate Breadth-First Search (BFS) or Depth-First Search (DFS) is initiated from every `1` cell to find the closest `0`.
    **Example**: If `mat[i][j]` is `1`, start a new BFS from `(i,j)` until a `0` is found.

-   **Concept**: Time Complexity of Naive Approach.
    **Context**: Performing a full BFS from each of the `M * N` cells (if all are `1`s) results in a high time complexity.
    **Example**: `O((M * N)^2)`. For `M*N = 10^4`, this is `(10^4)^2 = 10^8` operations, which is too slow for typical time limits.

-   **Concept**: Multi-Source Breadth-First Search (BFS) for Distance Problems.
    **Context**: The optimal and standard strategy for finding the shortest distance from *any* of multiple source points to all other points in an unweighted grid or graph.
    **Example**: Used when distances to the nearest `0` (from multiple `0`s) are needed for all `1`s.

-   **Concept**: BFS Initialization in Multi-Source BFS.
    **Context**: The BFS queue is initially populated with *all* source nodes (cells containing `0`s), as their distance to the nearest `0` is `0`.
    **Example**: `for r, c in matrix: if matrix[r][c] == 0: queue.append((r, c))`

-   **Concept**: Marking Unvisited Cells in Multi-Source BFS.
    **Context**: Cells that are `1` (and thus have unknown distances) are temporarily marked with a special value (e.g., `-1`) to distinguish them from `0`s and signify they are unvisited by the BFS wave.
    **Example**: `if mat[r][c] == 1: mat[r][c] = -1`.

-   **Concept**: Distance Calculation Rule in Multi-Source BFS.
    **Context**: During BFS traversal, the distance to a newly visited neighbor `(next_r, next_c)` is precisely one more than the distance of the current cell `(row, col)`.
    **Example**: `mat[next_row][next_col] = mat[row][col] + 1`.

-   **Concept**: Shortest Path Guarantee of BFS.
    **Context**: BFS inherently explores a graph layer by layer, ensuring that the very first time a particular cell is reached, it is always via the shortest possible path in an unweighted graph.
    **Example**: When `mat[next_row][next_col]` is updated to `mat[row][col] + 1`, this value is guaranteed to be the shortest distance from any `0`.

-   **Concept**: Time Complexity of Multi-Source BFS.
    **Context**: Each cell `(r, c)` in the `M x N` matrix is enqueued and dequeued at most once, with constant work performed for its 4 neighbors.
    **Example**: `O(M * N)`. This is efficient enough for `M*N <= 10^4`.

-   **Concept**: Space Complexity of Multi-Source BFS.
    **Context**: The primary space usage is for the queue, which in the worst case can hold all cells. The solution often modifies the input matrix in-place, avoiding additional output matrix space.
    **Example**: `O(M * N)` (for the `collections.deque` queue).

-   **Concept**: In-Place Modification for Space Optimization.
    **Context**: Reusing the input matrix to store the results and mark visited/unvisited states (e.g., using `-1` for unvisited `1`s) optimizes space by avoiding the need for a separate output matrix.

-   **Concept**: Dynamic Programming (DP) as Alternative for Grid Distance.
    **Context**: Another optimal approach for grid distance problems that typically involves multiple passes to correctly propagate distances from all cardinal directions.
    **Example**: A cell's `dist[r][c]` can be derived from `1 + min(dist[up], dist[left], dist[down], dist[right])`.

-   **Concept**: Two-Pass DP Strategy for Grid Distance.
    **Context**: A single pass (e.g., top-left to bottom-right) only accounts for dependencies from top and left neighbors. A second pass (bottom-right to top-left) is required to correctly incorporate dependencies from bottom and right neighbors.
    **Example**: Pass 1: `dist[r][c] = min(dist[r-1][c]+1, dist[r][c-1]+1)`. Pass 2: `dist[r][c] = min(dist[r][c], dist[r+1][c]+1, dist[r][c+1]+1)`.

-   **Concept**: Initialization for DP Grid Distance.
    **Context**: `0` cells are initialized to `0`. `1` cells are initialized to a very large number (infinity) to ensure any calculated path is shorter and propagates correctly.
    **Example**: `dist[r][c] = 0` for initial `0`s; `dist[r][c] = float('inf')` for initial `1`s.

-   **Concept**: Grid Traversal Directions (4-Way).
    **Context**: For problems involving movement to adjacent cells sharing an edge, a standard set of `(delta_row, delta_col)` tuples is used to explore neighbors.
    **Example**: `directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]` represents movement to down, up, right, and left cells respectively.

-   **Concept**: Performance with `M*N` Constraints.
    **Context**: For grid problems with `M*N` up to `10^4` (e.g., `100x100` or `1x10000`), an `O(M*N)` time complexity solution is essential and efficient enough.
    **Example**: An `O(M*N)` solution completes in roughly `10^4` operations, fitting within typical time limits (usually `10^8` ops/sec).

-   **Concept**: Handling Edge Cases in Grid Problems.
    **Context**: A robust solution should correctly handle various matrix configurations, including minimal dimensions, all source cells, or source cells isolated within target cells.
    **Example**: Test cases like `mat = [[0]]`, `mat = [[0,0],[0,0]]`, or `mat = [[1,1,1],[1,0,1],[1,1,1]]` are correctly handled by the Multi-Source BFS.