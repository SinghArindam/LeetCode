The problem asks us to transform a given `m x n` binary matrix `mat` into a new matrix where each cell `(i, j)` stores the shortest distance from `mat[i][j]` to its nearest `0`. The distance is defined as the number of steps required to move from one cell to an adjacent cell (sharing a common edge).

## 1. Problem Summary

Given an `m x n` binary matrix `mat` (containing `0`s and `1`s), we need to compute a new matrix of the same dimensions. For each cell `(r, c)` in the input matrix:
*   If `mat[r][c]` is `0`, its distance to the nearest `0` is `0`.
*   If `mat[r][c]` is `1`, we need to find the minimum number of steps (moving horizontally or vertically) to reach any cell containing `0`.
The problem guarantees that there is at least one `0` in the input matrix.

**Example:**
Input:
```
[[0,0,0],
 [0,1,0],
 [1,1,1]]
```
Output:
```
[[0,0,0],
 [0,1,0],
 [1,2,1]]
```
Here, the `1` at `mat[1][1]` is adjacent to three `0`s, so its distance is `1`. The `1` at `mat[2][0]` is adjacent to `mat[1][0]` (which is `0`), so its distance is `1`. The `1` at `mat[2][1]` is adjacent to `mat[2][0]` (which has distance `1`) and `mat[2][2]` (distance `1`). Its direct neighbors `mat[1][1]` (distance `1`) and `mat[2][0]` (distance `1`) and `mat[2][2]` (distance `1`) means the shortest path is from the `0` at `mat[1][1]` via `mat[1][0]` or `mat[2][0]`. Actually, it's easier to think that `mat[2][1]` is 1 step from `mat[1][1]` (distance 1) and `mat[2][0]` (distance 1) and `mat[2][2]` (distance 1). More precisely, from `mat[2][1]` you can go to `mat[1][1]` (distance 1), `mat[2][0]` (distance 1), `mat[2][2]` (distance 1). The actual values are then `min(dist(neighbor) + 1)`. `mat[1][1]` has distance `1` (from `mat[1][0]` or `mat[0][1]` or `mat[2][1]`), so `mat[2][1]` can be `1+dist(mat[1][1]) = 1+1=2`. `mat[2][0]` has distance `1` (from `mat[1][0]`). So `mat[2][1]` can be `1+dist(mat[2][0]) = 1+1=2`. The solution will correctly compute `2`.

## 2. Explanation of All Possible Approaches

### A. Naive Approach: BFS/DFS from Each '1' Cell

**Concept:**
For every cell `(r, c)` in the matrix:
1.  If `mat[r][c]` is `0`, its distance is `0`.
2.  If `mat[r][c]` is `1`, perform a Breadth-First Search (BFS) starting from `(r, c)`.
    *   During the BFS, explore neighbors level by level (each level representing an increment in distance).
    *   The first time a `0` cell is encountered, the current BFS level (which represents the distance) is the shortest distance for `mat[r][c]`.
    *   Use a `visited` set to avoid redundant computations and cycles within each BFS.

**Logic (as seen in the commented-out `Approach 1` in the provided solution):**
1. Initialize an output `dist_mat` of the same size as `mat`.
2. Iterate through each cell `(i, j)` of the `mat`.
3. If `mat[i][j] == 0`, set `dist_mat[i][j] = 0`.
4. If `mat[i][j] == 1`, start a new BFS:
    *   Initialize a `queue` with `(i, j)` and a `visited` set with `(i, j)`.
    *   Initialize `distance = 1`.
    *   While the `queue` is not empty:
        *   Process all nodes at the current `distance` level.
        *   For each current node `(curr_r, curr_c)`:
            *   Explore its 4 neighbors `(next_r, next_c)`.
            *   If a neighbor `(next_r, next_c)` is valid (in bounds) and not `visited`:
                *   Mark it `visited`.
                *   If `mat[next_r][next_c] == 0`, then `distance` is the answer for the starting `(i, j)`. Set `dist_mat[i][j] = distance` and break this BFS.
                *   Otherwise, add `(next_r, next_c)` to the queue.
        *   Increment `distance` for the next level.

**Complexity:**
*   **Time Complexity:** In the worst case, every cell is a `1`. For each of the `M * N` cells that are `1`, a full BFS might be performed, traversing up to `M * N` cells. Thus, the total time complexity would be `O((M * N)^2)`. Given `M * N <= 10^4`, `(10^4)^2 = 10^8` operations, which is too slow.
*   **Space Complexity:** For each BFS, we need `O(M * N)` for the `queue` and `visited` set. Total `O(M * N)` for the `dist_mat` as well.

### B. Optimal Approach 1: Multi-Source Breadth-First Search (BFS)

**Concept:**
This is the most efficient and standard approach for "distance from nearest X" problems on a grid. Instead of starting a BFS from each '1' cell, we initiate a single BFS simultaneously from *all* `0` cells. This effectively simulates a "wave" expanding outwards from all sources. When the wave reaches a `1` cell, it does so via the shortest path from *any* `0`.

**Logic (as seen in the active `Approach 2` in the provided solution):**
1.  **Initialization:**
    *   Create a queue (`collections.deque`) to hold cells to visit.
    *   Iterate through the input `mat`.
        *   If `mat[r][c]` is `0`: Add `(r, c)` to the `queue`. Its distance is `0`, so we leave `mat[r][c]` as `0`.
        *   If `mat[r][c]` is `1`: Change `mat[r][c]` to `-1`. This marks the cell as "unvisited" or "distance not yet calculated". It also prevents processing `0`s from the initial matrix as `1`s that need calculation later on.
2.  **BFS Traversal:**
    *   Define `directions` for 4-way movement: `[(1, 0), (-1, 0), (0, 1), (0, -1)]`.
    *   While the `queue` is not empty:
        *   Dequeue a cell `(row, col)`. `mat[row][col]` already holds its distance from the nearest `0`.
        *   For each of its 4 neighbors `(next_row, next_col)`:
            *   Check if `(next_row, next_col)` is within the matrix bounds.
            *   If it's in bounds AND `mat[next_row][next_col] == -1` (meaning it's an unvisited '1' cell):
                *   Set `mat[next_row][next_col] = mat[row][col] + 1`. This means the distance to this neighbor is one more than the distance to the current cell. Since BFS explores level by level, this is guaranteed to be the shortest distance.
                *   Enqueue `(next_row, next_col)` to process its neighbors later.
3.  **Result:** The modified `mat` now contains the calculated shortest distances for all cells.

**Complexity:**
*   **Time Complexity:** Each cell `(r, c)` is enqueued and dequeued at most once. When a cell is dequeued, its 4 neighbors are checked. Therefore, each cell is processed a constant number of times. Total time: `O(M * N)`.
*   **Space Complexity:** The maximum size of the queue can be `O(M * N)` (e.g., if the matrix is a checkerboard pattern of alternating 0s and 1s, or a border of 0s around 1s). The solution modifies the input matrix in place, so no additional `dist_mat` is needed. Thus, total space is `O(M * N)` (primarily for the queue).

### C. Optimal Approach 2: Dynamic Programming

**Concept:**
The shortest distance to a `0` for a cell `(r, c)` depends on the shortest distances of its adjacent cells. We can use dynamic programming by observing that `dist[r][c] = 1 + min(dist[neighbor])`. However, since a neighbor can be in any of the four directions (up, down, left, right), a single pass is not enough. We need two passes to propagate distances correctly.

**Logic:**
1.  **Initialization:**
    *   Create a `dist` matrix of the same size as `mat`.
    *   For `mat[r][c] == 0`, set `dist[r][c] = 0`.
    *   For `mat[r][c] == 1`, set `dist[r][c] = infinity` (a very large number, e.g., `rows * cols + 1` or `float('inf')`).
2.  **First Pass (Top-Left to Bottom-Right):**
    *   Iterate `r` from `0` to `rows-1`.
    *   Iterate `c` from `0` to `cols-1`.
    *   For each cell `(r, c)`:
        *   If `mat[r][c]` is `0`, skip (its distance is already `0`).
        *   Otherwise (if `mat[r][c]` is `1`):
            *   Consider neighbors from the top (`(r-1, c)`) and left (`(r, c-1)`).
            *   If `r > 0`, `dist[r][c] = min(dist[r][c], dist[r-1][c] + 1)`.
            *   If `c > 0`, `dist[r][c] = min(dist[r][c], dist[r][c-1] + 1)`.
    *   This pass correctly calculates distances for `1`s reachable from a `0` only by moving down or right.
3.  **Second Pass (Bottom-Right to Top-Left):**
    *   Iterate `r` from `rows-1` down to `0`.
    *   Iterate `c` from `cols-1` down to `0`.
    *   For each cell `(r, c)`:
        *   If `mat[r][c]` is `0`, skip.
        *   Otherwise:
            *   Consider neighbors from the bottom (`(r+1, c)`) and right (`(r, c+1)`).
            *   If `r < rows - 1`, `dist[r][c] = min(dist[r][c], dist[r+1][c] + 1)`.
            *   If `c < cols - 1`, `dist[r][c] = min(dist[r][c], dist[r][c+1] + 1)`.
    *   This pass corrects distances for `1`s that might be closer to a `0` by moving up or left. After these two passes, all shortest paths are considered.

**Complexity:**
*   **Time Complexity:** Two passes over the entire `M * N` matrix. Each cell takes constant time to process. Total: `O(M * N)`.
*   **Space Complexity:** `O(M * N)` for the `dist` matrix.

## 3. Detailed Explanation of the Provided Solution (Multi-Source BFS)

The provided solution implements the Multi-Source BFS approach, which is the most common and optimal way to solve this type of problem.

**Code Breakdown:**

```python
import collections
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Get the dimensions of the matrix.
        rows, cols = len(mat), len(mat[0])

        # Initialize a deque (double-ended queue) for BFS.
        # This queue will store the coordinates (r, c) of cells to be processed.
        queue = collections.deque()

        # First Pass: Initialize distances and populate the queue with all '0' cells.
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    # If a cell contains '0', its distance to the nearest '0' is 0.
                    # Add it to the queue as a starting point for the BFS.
                    queue.append((r, c))
                else:
                    # If a cell contains '1', it means its distance is yet to be determined.
                    # We mark it with -1 to signify "unvisited" or "distance unknown".
                    # This also prevents treating original '0's (which are 0) as '1's later.
                    mat[r][c] = -1 
        
        # Define the possible movements for neighbors (up, down, left, right).
        # dr, dc represent changes in row and column indices respectively.
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS Traversal:
        # The BFS proceeds in layers, ensuring that when a cell is visited,
        # it's reached via the shortest path from any of the initial '0' cells.
        while queue:
            # Dequeue the current cell (row, col).
            # mat[row][col] already stores its calculated shortest distance to a '0'.
            row, col = queue.popleft()

            # Explore all four possible neighbors of the current cell.
            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc

                # Check if the neighbor is within the matrix boundaries.
                is_in_bounds = 0 <= next_row < rows and 0 <= next_col < cols

                # If the neighbor is in bounds AND its distance hasn't been calculated yet (i.e., it's -1):
                if is_in_bounds and mat[next_row][next_col] == -1:
                    # Set the distance for this neighbor.
                    # Its distance is one more than the distance of the current cell.
                    # Since BFS guarantees finding the shortest path first, this value is final.
                    mat[next_row][next_col] = mat[row][col] + 1
                    
                    # Enqueue the neighbor to process its own neighbors in the next BFS level.
                    queue.append((next_row, next_col))
        
        # After the BFS completes, the 'mat' matrix itself contains the shortest distances
        # for all cells to their nearest '0'.
        return mat

```

**Why this approach is optimal:**

*   **Efficiency:** Each cell is added to the queue and processed exactly once. This leads to a linear time complexity proportional to the number of cells (`O(M * N)`).
*   **Correctness:** BFS inherently finds the shortest path in an unweighted graph (where all edge weights are 1, like in this grid problem). By starting from all `0`s simultaneously, it expands outwards in layers, guaranteeing that the first time a `1` cell is reached, it's via the minimum number of steps.
*   **Space Optimization:** By modifying the input `mat` in place, it uses minimal extra space beyond the queue itself.

## 4. Time and Space Complexity Analysis

### A. Naive Approach (BFS from Each '1' Cell)
*   **Time Complexity:** `O((M * N)^2)`
    *   In the worst case, every `1` cell triggers a full BFS traversal of the `M * N` grid.
*   **Space Complexity:** `O(M * N)`
    *   For the `dist_mat` to store results.
    *   Each BFS requires `O(M * N)` for its `queue` and `visited` set.

### B. Optimal Approach 1 (Multi-Source BFS) - Provided Solution
*   **Time Complexity:** `O(M * N)`
    *   Each cell is visited (enqueued and dequeued) at most once. For each cell, we perform constant work (checking its 4 neighbors).
*   **Space Complexity:** `O(M * N)`
    *   The `queue` can store up to `M * N` elements in the worst case (e.g., if the entire matrix needs to be processed).
    *   The solution modifies the input matrix in place, so no additional output matrix space is needed.

### C. Optimal Approach 2 (Dynamic Programming)
*   **Time Complexity:** `O(M * N)`
    *   Two passes over the entire `M * N` matrix. Each cell involves constant-time operations.
*   **Space Complexity:** `O(M * N)`
    *   For storing the `dist` matrix.

Both optimal approaches have the same `O(M*N)` time and space complexity, making them suitable for the given constraints. The BFS approach is generally more intuitive for shortest path problems on unweighted graphs.

## 5. Edge Cases

*   **Matrix with a single cell:**
    *   `mat = [[0]]` -> `[[0]]` (Correctly handled by initializing 0s in the queue).
    *   `mat = [[1]]` (Not possible due to constraint: "There is at least one 0 in mat").
*   **Matrix entirely composed of zeros:**
    *   `mat = [[0,0],[0,0]]` -> `[[0,0],[0,0]]` (Correctly handled. All cells are initially 0 and added to queue. Neighbors are also 0 and already have correct distances).
*   **Matrix with only one zero and surrounded by ones:**
    *   `mat = [[1,1,1],[1,0,1],[1,1,1]]` -> `[[2,1,2],[1,0,1],[2,1,2]]` (Handled correctly as BFS expands outwards from the central `0`).
*   **Constraints on dimensions:** `1 <= m, n <= 10^4` and `1 <= m * n <= 10^4`.
    *   This means `m` and `n` cannot both be large (e.g., `100x100` is `10^4` cells, but `10^4 x 10^4` is `10^8` cells, which exceeds the total cell count constraint). If `m=1`, `n` can be up to `10^4`. The `O(M*N)` solution handles these cases efficiently.

The Multi-Source BFS approach inherently handles all these cases correctly because it propagates distances outwards from all `0`s in an "onion-peeling" fashion, naturally finding the shortest path to every `1` cell.

## 6. Clean, Well-Commented Version of the Optimal Solution

```python
import collections
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Calculates the distance of the nearest 0 for each cell in a binary matrix.
        This problem is efficiently solved using a multi-source Breadth-First Search (BFS).

        The core idea is to start BFS simultaneously from all cells containing '0'.
        This ensures that when a '1' cell is first reached, it's via the shortest
        path from any of the '0's, as BFS explores layer by layer.

        Args:
            mat: An m x n binary matrix where '0' represents a source cell
                 and '1' represents a cell whose distance to the nearest '0' needs
                 to be calculated.

        Returns:
            A matrix of the same dimensions where each cell contains its shortest
            distance to the nearest '0'. The input matrix is modified in-place.
        """
        rows, cols = len(mat), len(mat[0])

        # Initialize a deque (double-ended queue) for the BFS.
        # This queue will hold the coordinates (r, c) of cells that are current
        # 'sources' or cells whose distance has just been determined and
        # whose neighbors need to be explored.
        queue = collections.deque()

        # Step 1: Initialize the matrix and the BFS queue.
        # Iterate through the entire matrix to identify all '0' cells (our starting points).
        # For '1' cells, we mark them as -1 to indicate they are unvisited/distance unknown.
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    # If the cell is '0', its distance to the nearest '0' is 0.
                    # Add it to the queue to start the BFS expansion from here.
                    # Its value in 'mat' remains 0.
                    queue.append((r, c))
                else:
                    # If the cell is '1', it means we need to find its distance.
                    # We temporarily set its value to -1. This serves two purposes:
                    # 1. Distinguishes it from '0's (sources) and actual distances.
                    # 2. Acts as a 'visited' marker for '1's that haven't been processed yet.
                    mat[r][c] = -1 
        
        # Define the possible movements for exploring neighbors (up, down, left, right).
        # These tuples represent (delta_row, delta_col).
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 2: Perform the Multi-Source BFS.
        # The BFS continues as long as there are cells in the queue to process.
        while queue:
            # Dequeue the current cell (row, col) from the front of the queue.
            # At this point, mat[row][col] already holds the minimum distance
            # from any '0' to this cell.
            row, col = queue.popleft()

            # Explore all four adjacent neighbors of the current cell.
            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc

                # Check if the neighbor coordinates are within the matrix boundaries.
                is_in_bounds = 0 <= next_row < rows and 0 <= next_col < cols

                # If the neighbor is in bounds AND its distance has not yet been calculated (i.e., it's -1):
                if is_in_bounds and mat[next_row][next_col] == -1:
                    # The distance to this neighbor is one more than the distance
                    # of the current cell. Since this is a BFS, we are guaranteed
                    # that the first time we reach mat[next_row][next_col], it's
                    # via the shortest path from *any* '0'. So, this distance is final.
                    mat[next_row][next_col] = mat[row][col] + 1
                    
                    # Add this newly processed neighbor to the queue. Its neighbors
                    # will be explored in the next 'layer' of the BFS.
                    queue.append((next_row, next_col))
        
        # After the BFS loop completes, all '1' cells will have been reached
        # from their nearest '0's, and their shortest distances will be stored
        # in the 'mat' matrix itself.
        return mat

```

## 7. Key Insights and Patterns

*   **Multi-Source BFS for Shortest Distance on Grids:** This is the most crucial takeaway. Whenever you need to find the shortest distance from *any* of a set of starting points (sources) to all other reachable points in an unweighted grid (where movement cost is uniform, e.g., 1 per step), a multi-source BFS is the go-to algorithm.
    *   **How it works:** Initialize the BFS queue with all source nodes, set their distances to 0. Then perform a standard BFS. Because BFS explores layer by layer, it naturally finds the shortest path.
    *   **Applicability:** Problems like "Shortest Path in Binary Matrix", "Map of Highest Peak" (which this problem is noted as being the same as), or finding distances to nearest obstacles/targets.
*   **Grid Traversal with BFS/DFS:** BFS is ideal for finding shortest paths in unweighted graphs (like grids where each step costs 1). DFS is typically used for path existence, connectivity, or finding all paths.
*   **In-Place Modification for Space Optimization:** Reusing the input matrix to store the results (e.g., by using special values like `-1` to mark unvisited cells) can save `O(M*N)` space, reducing overall space complexity.
*   **Dynamic Programming (Grid DP) as an Alternative:** While BFS is often more intuitive for shortest path, DP can also solve grid distance problems. It usually involves two passes (e.g., top-left to bottom-right, then bottom-right to top-left) to account for dependencies in all directions. This is a common pattern for problems where a cell's value depends on its immediate neighbors.
*   **Manhattan Distance (4-directional movement):** The problem's definition of "sharing a common edge" implies Manhattan distance (no diagonal moves). BFS naturally handles this by only exploring the four cardinal directions.