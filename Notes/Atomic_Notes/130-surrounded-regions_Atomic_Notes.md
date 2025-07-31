Here is a set of atomic notes for LeetCode problem 130 - Surrounded Regions, formatted for spaced repetition learning:

-   **Concept**: Problem Objective
    *   **Context**: Modify a 2D `board` (matrix of 'X' and 'O') in-place.
    *   **Example**: Change 'O' regions to 'X' if "surrounded".

-   **Concept**: Definition of "Surrounded" (Condition 1)
    *   **Context**: An 'O' region is considered "surrounded" if it is entirely enclosed by 'X' cells.
    *   **Example**: `[['X','O','X'],['X','O','X'],['X','X','X']]` - the inner 'O's are enclosed.

-   **Concept**: Definition of "Surrounded" (Crucial Condition 2)
    *   **Context**: An 'O' region is *not* surrounded if any of its 'O' cells are on the board's edge (border).
    *   **Example**: If `board[0][c] == 'O'`, that 'O' and any 'O's connected to it are considered "un-surrounded".

-   **Concept**: Core Strategy - Problem Inversion
    *   **Context**: It's easier to identify 'O's that are *NOT* surrounded, and then convert all other 'O's.
    *   **Example**: Instead of finding trapped 'O's, find 'O's that can "breathe" from the outside.

-   **Concept**: Phase 1: Identifying "Safe" 'O's
    *   **Context**: Start a graph traversal (DFS or BFS) from every 'O' cell located on the board's boundary.
    *   **Example**: If `board[row][0] == 'O'`, initiate a traversal from `(row, 0)`.

-   **Concept**: Phase 2: Temporary Marking
    *   **Context**: During traversal from border 'O's, change all reachable 'O' cells to a temporary marker character.
    *   **Example**: Change `board[r][c]` from 'O' to 'E' (or '#', 'S') to signify it's a "safe" 'O'.

-   **Concept**: Phase 3: Final Conversion
    *   **Context**: After marking all "safe" 'O's, iterate through the entire board.
    *   **Example**: Any cell still 'O' is truly surrounded and becomes 'X'; any temporary marker becomes 'O' again.

-   **Concept**: DFS (Depth-First Search) Application
    *   **Context**: Used for graph traversal on the grid, exploring deeply to find all connected "safe" 'O's.
    *   **Example**: Recursive function calls `dfs(next_r, next_c)` or using an explicit stack.

-   **Concept**: BFS (Breadth-First Search) Application
    *   **Context**: Used for graph traversal on the grid, exploring layer by layer to find all connected "safe" 'O's.
    *   **Example**: Using a `collections.deque` for a queue to manage cells to visit.

-   **Concept**: Time Complexity
    *   **Context**: For DFS/BFS-based solutions, the time complexity is linear with the number of cells.
    *   **Example**: `O(M * N)` because each cell is visited/processed a constant number of times.

-   **Concept**: Space Complexity
    *   **Context**: For DFS/BFS-based solutions, the worst-case space complexity is linear with the number of cells.
    *   **Example**: `O(M * N)` recursion stack depth or queue/stack size if the entire board is a single connected 'O' region.

-   **Concept**: Edge Case - Empty or Single-Cell Board
    *   **Context**: Handled by an initial check.
    *   **Example**: `if not board or not board[0]: return` correctly exits without errors or unnecessary operations.

-   **Concept**: Edge Case - Board Full of 'O's
    *   **Context**: All 'O's are connected to the border.
    *   **Example**: A `[['O','O'],['O','O']]` board remains unchanged, as no 'O's are truly surrounded.

-   **Concept**: General Pattern - Problem Inversion
    *   **Context**: A common strategy when direct identification of a property is hard; instead, identify its negation.
    *   **Example**: Finding elements *not* connected to a boundary instead of elements fully isolated.

-   **Concept**: General Pattern - Grid Traversal
    *   **Context**: DFS or BFS are fundamental algorithms for exploring connectivity, reachability, or flood-fill operations on 2D grids.
    *   **Example**: LeetCode problems like "Number of Islands" or "Max Area of Island".

-   **Concept**: General Pattern - Multi-Phase Processing
    *   **Context**: Breaking down a problem into sequential, distinct stages (e.g., initialization, core computation, final transformation).
    *   **Example**: This problem uses phases for marking, then for final conversion.

-   **Concept**: General Pattern - Temporary Markers
    *   **Context**: Using a temporary character or value within the data structure (like the `board` itself) to denote intermediate states of elements during processing.
    *   **Example**: Replacing 'O' with 'E' to mark "safe" cells.