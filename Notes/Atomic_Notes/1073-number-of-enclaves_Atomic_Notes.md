Here is a set of atomic notes for LeetCode problem 1073-number-of-enclaves, formatted for spaced repetition learning:

---

**Atomic Notes for LeetCode 1073: Number of Enclaves**

- **Concept**: Problem Definition - Number of Enclaves
  - **Context**: Given a binary grid, count land cells (1s) from which it's impossible to walk off the grid boundary.
  - **Example**: `[[0,1,1,0],[0,0,1,0],[0,0,0,0]]` -> The `1` at `grid[1][2]` is an enclave if `grid[0][2]` and `grid[2][2]` were also 0.

- **Concept**: Definition of an Enclave
  - **Context**: A land cell (and its connected land component) is an enclave if no part of that component is adjacent to the grid's boundary (row 0, row `m-1`, col 0, or col `n-1`) or can reach it through other land cells.
  - **Example**: In `[[0,0,0],[0,1,0],[0,0,0]]`, the `1` at `(1,1)` is an enclave.

- **Concept**: Movement Rule
  - **Context**: Movement between land cells is defined as 4-directionally adjacent (up, down, left, right).
  - **Example**: From `grid[r][c]`, valid moves are to `grid[r+1][c]`, `grid[r-1][c]`, `grid[r][c+1]`, `grid[r][c-1]`.

- **Concept**: Core Strategy - Inverse Logic (Complementary Counting)
  - **Context**: Instead of directly finding enclaves, find all land cells that *can* reach the boundary, mark them, and then count the remaining unmarked land cells.
  - **Example**: If 10 total land cells, and 7 are boundary-reachable, then 3 are enclaves.

- **Concept**: Optimal Approach - Flood Fill from Borders (General)
  - **Context**: The most efficient strategy for finding enclaved land cells is to start a graph traversal (DFS or BFS) from all land cells located on the grid's perimeter.
  - **Example**: Begin traversals from `grid[0][c]`, `grid[m-1][c]`, `grid[r][0]`, `grid[r][n-1]` if they are land cells.

- **Concept**: Flood Fill Mechanism - Marking Visited Cells (In-place)
  - **Context**: During a border-initiated traversal (DFS/BFS), change the value of visited land cells from `1` to `0` (or `2`). This effectively "sinks" them, preventing revisits and indicating they are not enclaves.
  - **Example**: If `grid[r][c]` is `1` and visited, set `grid[r][c] = 0`.

- **Concept**: Depth-First Search (DFS) for Flood Fill
  - **Context**: A recursive function `dfs_sink(row, col)` explores connected land cells. It has base cases for out-of-bounds or non-land cells, marks the current cell, and recursively calls itself for neighbors.
  - **Example**: `dfs_sink(r, c)` will call `dfs_sink(r+1, c)`, `dfs_sink(r-1, c)`, etc.

- **Concept**: Initializing Border Traversal
  - **Context**: All cells in the first row (`grid[0][:]`), last row (`grid[m-1][:]`), first column (`grid[:][0]`), and last column (`grid[:][n-1]`) are checked. If they contain land (`1`), a flood fill is started from them.
  - **Example**: `for r in range(m): if grid[r][0] == 1: dfs_sink(r,0)`

- **Concept**: Final Counting Step
  - **Context**: After all boundary-reachable land cells have been "sunk" (changed to `0`), iterate through the entire modified grid. Any remaining `1`s are enclaved land cells.
  - **Example**: `enclave_count = sum(sum(row_data) for row_data in grid)`

- **Concept**: Time Complexity of Flood Fill from Borders
  - **Context**: The algorithm visits each cell at most a constant number of times (initial check, traversal, final count).
  - **Example**: For an `M x N` grid, Time Complexity is `O(M * N)`.

- **Concept**: Space Complexity of Flood Fill from Borders (DFS)
  - **Context**: Dominated by the recursion stack for DFS. In the worst case (e.g., a snake-like path of `1`s), the recursion depth can be proportional to the total number of cells.
  - **Example**: For an `M x N` grid, Space Complexity is `O(M * N)`.

- **Concept**: Edge Case - Empty Grid
  - **Context**: If the grid has no rows or no columns, there are no land cells, so the count of enclaves is zero.
  - **Example**: `grid = []` or `grid = [[]]` should return `0`.

- **Concept**: Edge Case - Grid with 1 Row or 1 Column
  - **Context**: In a grid with only one row or one column, all land cells are by definition on the boundary. Therefore, no land cells can be enclaved.
  - **Example**: `[[1,1,1]]` or `[[1],[1],[1]]` will result in `0` enclaves.

- **Concept**: Edge Case - Grid Full of Sea (All 0s)
  - **Context**: If the grid contains no land cells, the count of enclaves is zero.
  - **Example**: `[[0,0],[0,0]]` returns `0`.

- **Concept**: Edge Case - Grid Full of Land (All 1s)
  - **Context**: If the grid is entirely land, all land cells are connected to the boundary. Thus, no land cells are enclaved.
  - **Example**: `[[1,1],[1,1]]` returns `0`.

- **Concept**: Handling Disconnected Land Masses
  - **Context**: The flood fill from borders correctly processes each connected component independently. Only components connected to the boundary will be "sunk"; isolated enclaved components remain untouched and are counted.
  - **Example**: A grid with `[[1,1,0],[1,1,0],[0,0,1]]` will sink the top-left `2x2` island if connected to border, leaving the bottom-right `1` if it's an enclave.

- **Concept**: Graph Traversal on Grids Pattern
  - **Context**: Many grid-based problems can be modeled as graph problems where cells are nodes and adjacency (4- or 8-directional) defines edges. DFS and BFS are primary tools.
  - **Example**: Finding connected components, shortest path in a maze, counting islands.

- **Concept**: Recursion Depth Limitation (Python)
  - **Context**: Recursive DFS in Python has a default recursion depth limit (e.g., 1000 or 3000). For very large grids, exceeding this limit can cause a `RecursionError`.
  - **Example**: For `M, N > 1000`, consider increasing `sys.setrecursionlimit()` or using an iterative BFS.

- **Concept**: Alternative - Breadth-First Search (BFS) for Flood Fill
  - **Context**: BFS uses a queue (e.g., `collections.deque`) instead of recursion, making it safer for very deep traversals by avoiding recursion depth limits. Functionally equivalent to DFS for this problem.
  - **Example**: Initialize queue with all border `1`s, then process layer by layer.

- **Concept**: Alternative - Disjoint Set Union (DSU)
  - **Context**: DSU can also solve connectivity problems by grouping connected elements into sets. While valid, it often has higher constant factors and more setup overhead for static grid problems compared to DFS/BFS.
  - **Example**: Could union all land cells with their land neighbors, and union border land cells with a special "border node." Then count land cells whose root is not the border node's root.