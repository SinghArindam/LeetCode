Here is a set of atomic notes for LeetCode problem 733, Flood Fill, suitable for spaced repetition learning:

---

-   **Concept**: Flood Fill Problem Goal
    -   **Context**: The primary objective of the Flood Fill algorithm.
    -   **Example**: To change the color of a connected component of pixels in an image grid, starting from a specified pixel `(sr, sc)`, to a `new_color`.

-   **Concept**: Flood Fill Connectivity Type
    -   **Context**: Defines how pixels are considered adjacent and part of the same component in Flood Fill.
    -   **Example**: Only 4-directional neighbors (up, down, left, right) are considered connected for the fill operation.

-   **Concept**: Flood Fill Pixel Selection Criterion
    -   **Context**: The condition a pixel must meet to be included in the connected component and have its color changed.
    -   **Example**: A pixel is part of the component if it has the *same original color* as the starting pixel `image[sr][sc]` *before* any changes are made.

-   **Concept**: Algorithmic Paradigm for Flood Fill
    -   **Context**: The general class of algorithms best suited for solving Flood Fill and similar grid problems.
    -   **Example**: Flood Fill is a classic **Graph Traversal** problem on a 2D grid, where grid cells are nodes and adjacencies are edges.

-   **Concept**: Optimal Graph Traversal Methods for Flood Fill
    -   **Context**: The specific algorithms commonly used and considered optimal for Flood Fill.
    -   **Example**: Both **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** are optimal and effective for this problem.

-   **Concept**: Depth-First Search (DFS) Principle
    -   **Context**: The core idea behind DFS as a graph traversal strategy.
    -   **Example**: DFS explores as far as possible along each branch from a node before backtracking; it is often implemented recursively.

-   **Concept**: DFS Application for Flood Fill
    -   **Context**: How DFS is applied to perform the flood fill operation.
    -   **Example**: A recursive helper function `dfs(r, c)` changes `image[r][c]` to `new_color` and then recursively calls itself for its 4 eligible neighbors.

-   **Concept**: DFS Base Case: Out of Bounds
    -   **Context**: A stopping condition for the recursive DFS in grid traversal.
    -   **Example**: If the current pixel `(r, c)` is outside the grid boundaries (`0 <= r < rows` or `0 <= c < cols`), the recursive call terminates.

-   **Concept**: DFS Base Case: Incorrect Color / Already Visited
    -   **Context**: A crucial stopping condition for the recursive DFS to correctly identify and avoid re-processing pixels.
    -   **Example**: If `image[r][c]` is *not* the `original_color` (meaning it's a different color or has already been changed to the `new_color`), the recursive call terminates.

-   **Concept**: Breadth-First Search (BFS) Principle
    -   **Context**: The core idea behind BFS as a graph traversal strategy.
    -   **Example**: BFS explores all the neighbor nodes at the present depth level before moving on to nodes at the next depth; it is typically implemented iteratively using a queue.

-   **Concept**: BFS Application for Flood Fill
    -   **Context**: How BFS is applied to perform the flood fill operation.
    -   **Example**: Use a queue initialized with `(sr, sc)`. In a loop, dequeue a pixel, change its color, and enqueue its 4 eligible neighbors.

-   **Concept**: Flood Fill Time Complexity
    -   **Context**: The time efficiency of both DFS and BFS solutions for Flood Fill.
    -   **Example**: O(M * N), where M is the number of rows and N is the number of columns, because each pixel is visited and processed at most once.

-   **Concept**: Flood Fill Space Complexity
    -   **Context**: The memory usage of both DFS and BFS solutions for Flood Fill.
    -   **Example**: O(M * N) in the worst case (e.g., an entire grid of the same color), due to the recursion stack depth for DFS or the queue size for BFS.

-   **Concept**: Flood Fill Edge Case: Start Color Equals New Color
    -   **Context**: A critical optimization and correctness check to handle a specific starting condition.
    -   **Example**: If `image[sr][sc] == color`, return the `image` immediately. This prevents infinite loops/recursion if `original_color` is already the target `new_color`, and avoids unnecessary traversal.

-   **Concept**: In-place Visited Marking (Flood Fill)
    -   **Context**: An efficient way to keep track of processed pixels in Flood Fill when modifying the grid is allowed.
    -   **Example**: Changing `image[r][c]` to the `new_color` implicitly marks it as "visited," as it will no longer match the `original_color` for subsequent checks.

-   **Concept**: Grid Traversal Boundary Checks
    -   **Context**: An essential practice in any algorithm that traverses a 2D grid.
    -   **Example**: Always ensure that coordinates `(r, c)` are within the valid range (`0 <= r < rows` and `0 <= c < cols`) before attempting to access `image[r][c]` to prevent `IndexError`.

-   **Concept**: Direction Arrays for Grid Traversal
    -   **Context**: A common pattern to simplify iterating over neighbors in grid-based algorithms.
    -   **Example**: Using a predefined array like `dirs = [[1,0], [-1,0], [0,1], [0,-1]]` to easily calculate the coordinates of 4-directional neighbors.