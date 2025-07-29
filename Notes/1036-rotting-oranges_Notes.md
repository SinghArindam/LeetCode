This document provides a comprehensive analysis of the LeetCode problem "Rotting Oranges", including problem summary, detailed explanations of various approaches, complexity analysis, edge case handling, a well-commented optimal solution, and key insights.

---

### 1. Problem Summary

You are given an `m x n` grid representing a farm of oranges. Each cell in the grid can have one of three values:
*   `0`: An empty cell.
*   `1`: A fresh orange.
*   `2`: A rotten orange.

The rules for rotting are:
*   Every minute, any fresh orange that is **4-directionally adjacent** (up, down, left, right) to a rotten orange becomes rotten.
*   The goal is to find the minimum number of minutes that must elapse until no cell contains a fresh orange.
*   If it's impossible for all fresh oranges to rot (i.e., some remain fresh forever), return `-1`.

**Constraints:**
*   `1 <= m, n <= 10` (Grid dimensions are small, up to 10x10)
*   `grid[i][j]` is `0`, `1`, or `2`.

---

### 2. Explanation of All Possible Approaches

This problem involves a spreading process on a grid, where the goal is to find the minimum time for the spread to complete. This is a classic indicator for Breadth-First Search (BFS) on an unweighted graph, especially a multi-source BFS.

#### 2.1 Naive Simulation / Iterative Grid Scan

One intuitive way to approach this is to simulate the process minute by minute.

**Logic:**
1.  Initialize `minutes = 0`.
2.  In a loop, for each minute:
    a.  Identify all fresh oranges that will rot in this minute. This means they are adjacent to a *currently* rotten orange.
    b.  It's crucial to identify all such oranges *before* changing the grid, because if you change `grid[x][y]` to rotten in place, it might incorrectly cause its neighbor to rot in the *same* minute, when it should rot in the *next* minute. Therefore, you need a way to store the oranges that will rot in the current minute, or mark them temporarily.
    c.  After identifying all oranges that will rot, update their status to `2` (rotten).
    d.  If no oranges rotted in this minute, break the loop.
    e.  Increment `minutes`.
3.  After the loop, iterate through the grid one last time. If any fresh oranges (`1`) remain, return `-1`. Otherwise, return `minutes`.

**Example of Implementation Strategy (Similar to commented-out Approach 1 in provided code):**
Instead of a separate list for newly rotten oranges, one could use modified values in the grid itself to encode the time an orange became rotten. For example, `grid[i][j] = k` could mean this orange rotted at minute `k-2`. Fresh oranges are `1`. Then, in each iteration (`elapsedTime`), you look for oranges that rotted at `elapsedTime + 2` (i.e., current `elapsedTime` from start), and use them to rot their fresh neighbors. New neighbors would be marked `(elapsedTime + 1) + 2`.

**Critique:**
*   **Correctness:** Can be made correct with careful state management (e.g., using a temporary grid or marking new rotten oranges with a distinct value for the current minute). The provided "Approach 1" uses `grid[i][j] == elapsedTime + 2` to identify the "source" oranges for the current minute, and then marks fresh neighbors with `grid[i][j] + 1`, effectively marking them for the next minute. This cleverly uses the grid values as "distance" from the initial rotten oranges.
*   **Efficiency:** This approach involves scanning the entire `M x N` grid in each minute. In the worst case, an orange might take `M + N` minutes to rot (e.g., if it's at one corner and rotten oranges are at the opposite corner and have to spread diagonally). This leads to a time complexity of O(M*N * (M+N)) or O((M*N)^2) in general, which is not optimal for larger grids.

#### 2.2 Depth-First Search (DFS)

**Logic:**
A standard DFS is generally not suitable for "shortest path" or "minimum time" problems on unweighted graphs because it explores depth-first, meaning it might find a long path to a cell before finding a shorter one. While it's possible to adapt DFS to behave like Dijkstra's (by updating minimum times and revisiting if a shorter path is found, as attempted in commented-out Approach 2), it's typically less efficient than BFS for this specific type of problem due to potential for repeated computations and recursion stack overhead.

**Critique:**
*   **Correctness:** Can be made correct, but requires careful handling of visited states and minimum time updates, which often makes it more complex than BFS. The `grid[x][y] > time + 1` condition in Approach 2 attempts to ensure correctness by only updating if a shorter path is found.
*   **Efficiency:** The recursive nature and potential for revisits make it generally less efficient for this problem than BFS. Worst-case time complexity could still be O(M*N) if effectively behaving like a BFS/Dijkstra, but practically slower due to function call overhead.

#### 2.3 Breadth-First Search (BFS) - Optimal Approach

This is the most suitable and optimal approach for this problem.

**Logic:**
1.  **Initialization:**
    *   Identify all initial rotten oranges (value `2`). These are the starting points for our BFS. Add their coordinates `(row, col)` to a queue.
    *   Count the total number of `fresh` oranges (value `1`). We need to ensure all of them rot.
    *   Initialize `minutes = 0`.
2.  **Edge Case:** If `num_of_fresh == 0` at the start, no time is needed, return `0`.
3.  **BFS Traversal:**
    *   While the queue is not empty AND there are still fresh oranges to rot (`num_of_fresh > 0`):
        *   This loop represents progressing minute by minute.
        *   Get the `size` of the queue *at the beginning of the current minute*. This is crucial for level-by-level processing in BFS. All oranges in the queue *at this moment* will rot their neighbors in the *current* minute.
        *   Iterate `size` times:
            *   Dequeue an orange `(r, c)`.
            *   For each of its 4-directionally adjacent neighbors `(nr, nc)`:
                *   Check if `(nr, nc)` is within grid boundaries.
                *   Check if `grid[nr][nc]` is a fresh orange (`1`).
                *   If both conditions are true:
                    *   Mark `grid[nr][nc]` as rotten (`2`).
                    *   Decrement `num_of_fresh`.
                    *   Enqueue `(nr, nc)`. These newly rotten oranges will act as sources for the *next* minute.
        *   After processing all oranges from the current minute's level, increment `minutes`.
4.  **Final Check:**
    *   After the BFS loop finishes:
        *   If `num_of_fresh > 0`, it means some fresh oranges are unreachable and will never rot. Return `-1`.
        *   Otherwise (all fresh oranges have rotted), return `minutes`.

**Critique:**
*   **Correctness:** Guaranteed to find the minimum time because BFS explores layer by layer, ensuring the shortest path (minimum time) to each orange.
*   **Efficiency:** Optimal. Each cell is visited and processed at most a constant number of times (added to queue, dequeued, its neighbors checked).

---

### 3. Detailed Explanation of the Logic Behind the Provided Solution and Any Alternative Approaches

The provided solution code includes three approaches, two of which are commented out. Let's analyze them:

#### 3.1 Provided Optimal Solution (Approach 3 - Multi-Source BFS)

This is the standard, optimal BFS approach described in Section 2.3.

**Logic Breakdown:**

1.  **Initialization:**
    ```python
    n, m = len(grid), len(grid[0])
    num_of_fresh = 0
    ls_rotten = [] # This list serves as our BFS queue
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                ls_rotten.append((i, j)) # Add initial rotten oranges to the queue
            if grid[i][j] == 1:
                num_of_fresh += 1 # Count initial fresh oranges
    ```
    *   `n`, `m`: Dimensions of the grid.
    *   `num_of_fresh`: Counter for fresh oranges. Decremented as oranges rot.
    *   `ls_rotten`: A list acting as a queue (using `pop(0)` for dequeue). It stores `(row, col)` coordinates of rotten oranges that are active sources for the current minute.

2.  **Base Case/Edge Case:**
    ```python
    if num_of_fresh == 0:
        return 0 # If no fresh oranges, 0 minutes needed.
    ```
    *   Handles scenarios like `[[0,2]]`, `[[0,0]]`, or `[[2,2]]` where there are no fresh oranges to begin with.

3.  **BFS Loop:**
    ```python
    t = 0 # Time elapsed, represents minutes
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]] # Directions for 4-directional adjacency

    while ls_rotten and num_of_fresh > 0:
        num_rotten_curr_level = len(ls_rotten) # Get count of oranges rotting at THIS minute
        for z in range(num_rotten_curr_level):
            i, j = ls_rotten.pop(0) # Dequeue an orange from current level
            for dr in dirs:
                x = i + dr[0]
                y = j + dr[1]
                # Check bounds and if neighbor is a fresh orange
                if (0 <= x < n and 0 <= y < m) and (grid[x][y] == 1):
                    grid[x][y] = 2 # Mark as rotten (important: modifies grid in-place)
                    num_of_fresh -= 1 # Decrement fresh orange count
                    ls_rotten.append((x, y)) # Add to queue for next minute's processing
        t += 1 # Increment minute after processing all oranges for the current level
    ```
    *   The `while` loop continues as long as there are rotten oranges to spread from (`ls_rotten` is not empty) and there are still fresh oranges remaining (`num_of_fresh > 0`).
    *   `num_rotten_curr_level` ensures that we process *only* the oranges that became rotten in the *previous* minute in the current iteration. This is the core mechanism of level-by-level BFS.
    *   `ls_rotten.pop(0)` is used to dequeue, making `ls_rotten` behave like a queue.
    *   When a fresh orange is found, it's marked `2` (rotten), `num_of_fresh` is decremented, and it's added to the queue to be processed in the *next* minute.
    *   `t` increments only *after* a full "layer" of rotting has occurred.

4.  **Final Result:**
    ```python
    if num_of_fresh > 0:
        return -1 # If fresh oranges remain, it's impossible
    return max(0, t) # Otherwise, return total minutes. max(0,t) handles initial t=0 case.
    ```
    *   If the loop terminates because `num_of_fresh` is still greater than 0, it means some oranges were unreachable.
    *   `max(0, t)`: This is slightly redundant if `num_of_fresh == 0` is handled upfront, as `t` will correctly be 0 in that case. However, it doesn't hurt. For `t` to be greater than 0, at least one minute must have passed. If no rotting occurs (`ls_rotten` is empty and `num_of_fresh > 0`), the loop doesn't run and `t` remains 0, which would then incorrectly return 0 when it should be -1. But `num_of_fresh > 0` condition handles that. So `return t` is generally sufficient here.

#### 3.2 Alternative Approach 1 (Commented Out - Iterative Simulation with Time Encoding)

```python
# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         def isSafe(i, j, n, m):
#             return 0 <= i < n and 0 <= j < m
#         n = len(grid)
#         m = len(grid[0])
#         changed = False # Flag to check if any orange rotted in current minute
#         elapsedTime = 0 # Current minute counter
#         directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
#         while True:
#             # Create a list of oranges that will rot in this minute
#             # We iterate over the grid to find oranges that *just* rotted at `elapsedTime`.
#             # Their value in grid would be `elapsedTime + 2` (initial rotten are 2, then 3, 4, etc.)
#             oranges_to_spread_from = []
#             for i in range(n):
#                 for j in range(m):
#                     if grid[i][j] == elapsedTime + 2:
#                         oranges_to_spread_from.append((i, j))
            
#             # If no oranges to spread from for this minute, and no fresh oranges became rotten
#             # in the previous step, then we break.
#             if not changed and elapsedTime > 0: # If nothing changed in the previous minute, and not first minute
#                 break
#             if not oranges_to_spread_from and elapsedTime > 0: # No new oranges to spread from
#                 break
            
#             current_minute_changed = False
#             newly_rotten_coords = [] # Store coordinates of oranges that will rot in this minute
            
#             # Iterate over all oranges identified as sources for this minute
#             for i, j in oranges_to_spread_from:
#                 for dir in directions:
#                     x = i + dir[0]
#                     y = j + dir[1]
#                     if isSafe(x, y, n, m) and grid[x][y] == 1: # If neighbor is fresh
#                         # Mark it with a value that indicates it rotted at `elapsedTime + 1`
#                         # (grid[i][j] + 1 would be (elapsedTime + 2) + 1 = elapsedTime + 3)
#                         grid[x][y] = grid[i][j] + 1
#                         current_minute_changed = True
            
#             changed = current_minute_changed
#             if not changed and elapsedTime > 0: # No oranges rotted in this minute
#                 break
#             if not changed and elapsedTime == 0 and not oranges_to_spread_from: # special initial empty case
#                 break

#             elapsedTime += 1
        
#         # Final check for any remaining fresh oranges
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 1:
#                     return -1
        
#         # Special adjustment for elapsedTime: if no oranges ever rotted, elapsedTime would be 0, which is correct.
#         # If there were initial rotten oranges and they started spreading, elapsedTime counts correctly.
#         # But the loop condition might add an extra minute if the last change happens just before breaking.
#         # The logic needs careful checking for the exact count.
#         # The original `while True` loop and `changed` flag for breaking:
#         # It increments `elapsedTime` *after* checking. If `elapsedTime` is 0 initially, it looks for `grid[i][j] == 2`.
#         # If `changed` is False after that initial pass, it means no fresh oranges were adjacent to initial rotten.
#         # So it breaks, and `elapsedTime` is still 0. This seems correct.
#         # Let's consider [[2,1,1],[1,1,0],[0,1,1]].
#         # t=0: sources = initial [2]. grid values become 3 for neighbors. changed=True. t becomes 1.
#         # t=1: sources = oranges that are 3. grid values become 4 for neighbors. changed=True. t becomes 2.
#         # ...
#         # The max value in the grid minus 2 will be the max time. If no rotting happened, max value is 2, time is 0.
#         # If it stopped because no new oranges rotted, the last `elapsedTime` before break is the answer.
#         # The original commented approach is a bit tricky with `changed` flag. It seems to have a bug in how `changed` is reset/used.
#         # The structure `if not changed: break; changed = False; elapsedTime += 1` means `elapsedTime` is incremented *after* `changed` has been determined for the current minute.
#         # If `changed` is false, it breaks, and `elapsedTime` is the correct value.
#         # If `elapsedTime` is 0 and there are initial rotten oranges, `changed` will be True. `elapsedTime` becomes 1.
#         # The final return of `elapsedTime` seems correct based on this structure.
#         return elapsedTime
```
**Logic Breakdown (Corrected understanding of provided commented code):**
This approach iteratively simulates the rotting process. Each cell `grid[i][j]` stores not just `0`, `1`, `2`, but `2 + minutes_to_rot`, effectively marking the time an orange turned rotten.
1.  **Initialization**: `elapsedTime = 0`. `changed = False` (to track if any orange rotted in the current `elapsedTime` pass).
2.  **Main Loop (`while True`):** Represents minutes passing.
    *   Iterate through the `grid`. If `grid[i][j]` is equal to `elapsedTime + 2`, it means this orange turned rotten *exactly* `elapsedTime` minutes ago (i.e., it's a "source" for the *current* minute's spreading).
    *   For such sources, check their 4-directional neighbors. If a neighbor `(x, y)` is fresh (`grid[x][y] == 1`), then:
        *   Mark it as rotten *for the next minute*: `grid[x][y] = grid[i][j] + 1` (which is `(elapsedTime + 2) + 1 = elapsedTime + 3`). This effectively sets its "rotting time" to `elapsedTime + 1`.
        *   Set `changed = True` because at least one orange rotted in this pass.
    *   **Break Condition**: If `changed` is `False` after checking *all* cells for the current `elapsedTime`, it means no new oranges rotted. So, the process has stopped. Break the loop.
    *   **Reset and Increment**: Reset `changed = False` for the next pass and increment `elapsedTime`.
3.  **Final Check**: After the loop, iterate through the grid. If any `grid[i][j] == 1` (fresh orange remains), return `-1`. Otherwise, return `elapsedTime`.

**Critique:**
*   **Correctness:** This approach correctly determines the minimum time by effectively simulating a BFS using the grid values as time markers. The key is that it only spreads from oranges that *just* rotted (value `elapsedTime + 2`), ensuring level-by-level processing.
*   **Efficiency:** This is less efficient than the queue-based BFS (Approach 3). In each minute (`elapsedTime` loop), it scans the *entire* `M x N` grid to find the sources for that minute. If `K` is the maximum minutes (which can be up to `M+N` in worst case), the total time complexity is O(M*N*K) = O(M*N*(M+N)).

#### 3.3 Alternative Approach 2 (Commented Out - Recursive DFS with Time Update)

```python
# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         def is_safe(i, j, n, m):
#             return 0 <= i < n and 0 <= j < m
#         def dfs(grid, i, j, time):
#             n = len(grid)
#             m = len(grid[0])
#             grid[i][j] = time # Mark current orange with its rotting time
#             directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
#             for dir in directions:
#                 x = i + dir[0]
#                 y = j + dir[1]
#                 # Check if neighbor is safe and either:
#                 # 1. It's a fresh orange (grid[x][y] == 1) OR
#                 # 2. It's already marked as rotten but this path offers a FASTER rotting time
#                 if is_safe(x, y, n, m) and (grid[x][y] == 1 or grid[x][y] > time + 1):
#                     dfs(grid, x, y, time + 1) # Recurse for neighbor with incremented time
        
#         n = len(grid)
#         m = len(grid[0])
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 2:
#                     dfs(grid, i, j, 2) # Start DFS from all initial rotten oranges
        
#         elapsed_time = 0
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 1:
#                     return -1 # Found an unrotted fresh orange
#                 # Calculate max elapsed time. If grid[i][j] is 0 or 2, then time is 0.
#                 # Otherwise, it's (time it rotted + 2). So subtract 2.
#                 elapsed_time = max(elapsed_time, grid[i][j] - 2)
#         return elapsed_time
```
**Logic Breakdown:**
This approach uses DFS to propagate the rotting process, attempting to find the minimum time for each orange to rot.
1.  **`dfs(grid, i, j, time)` function:**
    *   This recursive function attempts to rot oranges starting from `(i, j)` at a given `time`.
    *   `grid[i][j] = time`: The current orange is marked with the `time` it becomes rotten. Initial rotten oranges start with `time = 2`.
    *   It explores 4-directional neighbors.
    *   The crucial condition `(grid[x][y] == 1 or grid[x][y] > time + 1)`:
        *   `grid[x][y] == 1`: If the neighbor is fresh, it can be rotted.
        *   `grid[x][y] > time + 1`: If the neighbor is *already rotten* (`> 2`), but its current `grid` value indicates it rotted *later* than `time + 1` (meaning this new path is shorter), then it's revisited and updated. This makes it behave somewhat like a Dijkstra's shortest path algorithm for unweighted graphs, where you update a distance if a shorter one is found.
    *   `dfs(grid, x, y, time + 1)`: Recursively calls for the neighbor with an incremented time.

2.  **Main Logic:**
    *   Iterate through the grid to find all initial rotten oranges (`grid[i][j] == 2`).
    *   For each initial rotten orange, start a `dfs` call with `time = 2`.
    *   After all initial DFS calls complete, iterate through the grid again:
        *   If any `grid[i][j] == 1`, return `-1`.
        *   Otherwise, calculate `elapsed_time` as the maximum of `grid[i][j] - 2` for all cells. This effectively finds the maximum "distance" from an initial rotten orange.

**Critique:**
*   **Correctness:** This approach can be correct for finding shortest paths on an unweighted graph, but it's not a typical BFS. The re-visiting logic (`grid[x][y] > time + 1`) ensures that if a shorter path to an orange is found, its `time` value is updated.
*   **Efficiency:** While the concept can work, recursive DFS on a grid that modifies states and revisits can be less efficient than an iterative BFS. Without memoization or a proper `visited` set that marks *finalized* shortest paths, it might explore redundant paths, leading to higher constant factors or even worse worst-case if not implemented carefully (e.g., if the depth of recursion gets very large, potentially M*N). However, for an unweighted graph, each node is pushed onto the stack (visited) at most `degree` times in worst case if `grid[x][y] > time + 1` is the only check, which still results in a total of O(V+E) where V=M*N and E=4*M*N, so O(MN).

---

### 4. Time and Space Complexity Analysis

Let `N` be the number of rows (`m`) and `M` be the number of columns (`n`) in the grid.
Total cells = `R * C` (or `m * n`).

#### 4.1 Optimal Approach (Approach 3 - Multi-Source BFS)

*   **Time Complexity: O(R * C)**
    *   **Initialization:** Iterating through the grid to find initial rotten oranges and count fresh ones takes O(R * C).
    *   **BFS Traversal:** Each cell in the grid is visited and processed at most a constant number of times:
        *   It's added to the queue at most once.
        *   It's dequeued at most once.
        *   When dequeued, its 4 neighbors are checked.
    *   Therefore, the total time for BFS is proportional to the number of cells, O(R * C).
*   **Space Complexity: O(R * C)**
    *   **Queue (`ls_rotten`):** In the worst case (e.g., a checkerboard pattern of all oranges or all oranges become rotten), the queue can hold up to O(R * C) coordinates.
    *   **`grid` modification:** Done in-place, so no additional grid space.

#### 4.2 Alternative Approach 1 (Iterative Simulation with Time Encoding)

*   **Time Complexity: O(R * C * (R + C))**
    *   The outer `while` loop runs for `K` iterations, where `K` is the maximum number of minutes an orange might take to rot. In the worst case, `K` can be up to `R + C - 2` (e.g., spreading diagonally from one corner to another).
    *   Inside the `while` loop, the entire `R * C` grid is iterated through in each minute to find the sources.
    *   Total time: O(R * C * K) = O(R * C * (R + C)).
*   **Space Complexity: O(1)**
    *   The grid is modified in-place. A few variables are used. No additional data structures whose size depends on R or C, beyond the input grid itself.

#### 4.3 Alternative Approach 2 (Recursive DFS with Time Update)

*   **Time Complexity: O(R * C)**
    *   Each cell's `dfs` call involves checking its 4 neighbors. Due to the condition `grid[x][y] > time + 1`, a cell will only be "revisited" if a strictly shorter path is found. In an unweighted graph, this mechanism ensures that each cell is effectively processed in a way similar to BFS or Dijkstra's, where its "shortest time" is finalized or improved upon. Thus, each cell's `dfs` execution (and its neighbors' checks) effectively contributes a constant amount of work on average. Total work is proportional to the number of cells and edges (M*N cells, 4*M*N edges).
    *   Practically, recursion overhead might make it slower than iterative BFS.
*   **Space Complexity: O(R * C)**
    *   **Recursion Stack:** In the worst case (e.g., a long path, or a grid filled with fresh oranges that rot in a chain), the recursion depth can go up to O(R * C), requiring O(R * C) stack space.

---

### 5. Edge Cases and How They Are Handled

1.  **No Fresh Oranges Initially:**
    *   **Example:** `grid = [[0,2]]`, `grid = [[0,0]]`, `grid = [[2,2,0]]`
    *   **Handling:** The optimal solution (`Approach 3`) explicitly checks `if num_of_fresh == 0: return 0`. This correctly returns `0` minutes, as no rotting needs to occur.
2.  **No Rotten Oranges Initially, But Fresh Oranges Exist:**
    *   **Example:** `grid = [[1,1],[1,0]]`
    *   **Handling:** `ls_rotten` will be empty. The `while ls_rotten and num_of_fresh > 0` loop will not execute because `ls_rotten` is empty. `num_of_fresh` will still be `> 0`. The final `if num_of_fresh > 0: return -1` correctly returns `-1`.
3.  **Some Fresh Oranges are Unreachable:**
    *   **Example:** `grid = [[2,1,1],[0,1,1],[1,0,1]]` (the orange at `[2][0]` is isolated).
    *   **Handling:** The BFS will complete, but `num_of_fresh` will still be `> 0` because the unreachable oranges were never added to the queue or marked rotten. The final `if num_of_fresh > 0: return -1` correctly returns `-1`.
4.  **Single Cell Grid:**
    *   `grid = [[0]]`: `num_of_fresh = 0`, returns `0`. Correct.
    *   `grid = [[1]]`: `num_of_fresh = 1`, `ls_rotten = []`. Loop not entered. Returns `-1`. Correct.
    *   `grid = [[2]]`: `num_of_fresh = 0`, returns `0`. Correct.
5.  **All Oranges Rot at the Same Time / Minimal Rotting Time:**
    *   **Example:** `grid = [[2,1,2]]`
    *   **Handling:** `t` will increment to 1. `num_of_fresh` will become 0. Returns 1. Correct.
    *   Example: `grid = [[2,1],[1,1]]` (this takes 2 minutes)
    *   **Handling:** The BFS correctly processes layers, `t` increments twice, `num_of_fresh` becomes 0. Returns 2. Correct.

---

### 6. Clean, Well-Commented Version of the Optimal Solution

```python
from collections import deque # Using deque for efficient pop(0)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Calculates the minimum time required for all fresh oranges to rot.
        Uses a multi-source Breadth-First Search (BFS) approach.
        """
        
        R, C = len(grid), len(grid[0])
        
        # Initialize queue with all initially rotten oranges
        # Count the total number of fresh oranges
        rotten_queue = deque() # Stores (row, col) of rotten oranges
        fresh_oranges_count = 0
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    rotten_queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges_count += 1
        
        # Edge case: If there are no fresh oranges initially, 0 minutes are needed.
        if fresh_oranges_count == 0:
            return 0
            
        minutes = 0 # Stores the elapsed time
        
        # Define directions for 4-directional adjacency (up, down, left, right)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # BFS traversal: Process layer by layer (each layer represents 1 minute)
        # Continue as long as there are rotten oranges to spread from AND fresh oranges remaining
        while rotten_queue and fresh_oranges_count > 0:
            # Get the number of rotten oranges at the current level (minute)
            # This ensures we process all oranges that rot in THIS minute
            current_level_size = len(rotten_queue)
            
            # Process all oranges from the current minute's "wave"
            for _ in range(current_level_size):
                r, c = rotten_queue.popleft() # Dequeue an orange
                
                # Check all 4 neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check if the neighbor is within grid boundaries and is a fresh orange
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                        grid[nr][nc] = 2          # Mark the fresh orange as rotten
                        fresh_oranges_count -= 1  # Decrement the count of fresh oranges
                        rotten_queue.append((nr, nc)) # Add newly rotten orange to queue for next minute
            
            # If any oranges rotted in this minute, increment the minute counter
            # This check prevents incrementing minutes if the queue was just emptied
            # without new oranges being added (e.g., if fresh_oranges_count became 0)
            # or if the queue was empty at the start of the loop iteration.
            # However, the loop condition `rotten_queue and fresh_oranges_count > 0`
            # implicitly handles this logic. If the inner loop executed, it means
            # current_level_size > 0, so at least one orange was processed.
            if len(rotten_queue) > 0 or fresh_oranges_count == 0: # Check if propagation happened or all rotted
                 minutes += 1
            else: # If queue became empty AND fresh oranges still remain, propagation stopped.
                break 

        # Final check:
        # If there are still fresh oranges left, it's impossible for them to rot.
        if fresh_oranges_count > 0:
            return -1
        else:
            # All fresh oranges have rotted. Return the total minutes elapsed.
            # Note: `minutes` will be 0 if `fresh_oranges_count` was initially 0,
            # which is correctly handled by the initial check.
            # If no oranges ever rotted (e.g. [[1,1]]), minutes remains 0,
            # and fresh_oranges_count > 0, so it correctly returns -1.
            # The last `minutes += 1` might overcount by 1 if the last fresh orange rotted
            # and the queue is now empty and no new oranges were added.
            # A common pattern is to increment minutes *before* checking the queue size for the next level,
            # but that means handling the initial minute more carefully.
            # The current approach correctly tracks minutes as "layers".
            # The `if len(rotten_queue) > 0 or fresh_oranges_count == 0:` condition
            # helps ensure we only increment minutes if progress was made.
            # Example [[2,1,1],[1,1,0],[0,1,1]] -> Output 4.
            # At minute 4, last oranges rot. Queue becomes empty. `minutes` becomes 4.
            # `fresh_oranges_count` becomes 0. Loop terminates. Returns 4. Correct.
            return minutes

```
**Correction/Refinement on `minutes` increment logic for the BFS template:**
The typical BFS template for level-by-level processing has `minutes` increment *after* a full level is processed. The provided solution's commented-out `print` statements suggest `t` increments *after* processing oranges from `t` and setting `t+1` oranges. This is standard.

The line `if len(rotten_queue) > 0 or fresh_oranges_count == 0: minutes += 1` in the clean code is a slight deviation that might be overly cautious or slightly confusing. A simpler standard approach is:

```python
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        q = collections.deque()
        fresh_count = 0
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
            
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q: # While there are rotten oranges to spread from
            # Process all oranges that are currently rotten and can spread in this minute
            size = len(q)
            rotted_in_this_minute = False # Flag to track if any fresh orange rotted in this minute
            
            for _ in range(size):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                        grid[nr][nc] = 2          # Mark as rotten
                        fresh_count -= 1          # Decrement fresh count
                        q.append((nr, nc))        # Add to queue for next minute
                        rotted_in_this_minute = True # Set flag
            
            # After processing all oranges from the current level:
            # If any orange rotted in this minute OR if the queue is now empty but all fresh oranges rotted,
            # this means a full minute has passed for propagation.
            # This condition ensures `minutes` only increments if actual rotting occurred in the current layer.
            # Or if it's the last layer and all fresh oranges are processed.
            # A simpler way: if the queue is not empty after this level (meaning new oranges were added)
            # OR if fresh_count is 0 and we JUST processed the last ones.
            # The most straightforward way in BFS: increment `minutes` if `q` is not empty *after* processing
            # a level, because that means there's a *next* level.
            if q and fresh_count > 0: # Only increment minutes if there are more oranges to process in the future
                minutes += 1
            elif fresh_count == 0: # All oranges rotted, the current minutes is the answer
                return minutes
            else: # q is empty and fresh_count > 0. Means unreachable.
                break
        
        # If loop finishes and fresh oranges remain (q became empty but fresh_count > 0)
        if fresh_count > 0:
            return -1
        else:
            return minutes # All rotted, minutes is correct

```
The provided solution's original `t+=1` outside the loop, but inside the `while` block, effectively means `t` is the number of layers processed. It only increments `t` if `ls_rotten` (the queue) was not empty, and fresh oranges were still pending. The `if len(ls_rotten) > 0 or fresh_oranges_count == 0` for incrementing minutes in my improved version above is a common pattern to avoid overcounting the last minute if the `queue` becomes empty, but the `fresh_oranges_count` check handles cases where the `queue` runs out of active rotten oranges before all fresh oranges are gone. The original solution's `t+=1` before `break` is cleaner.

Final analysis of the given `t+=1` in the provided solution:
```python
        t=0
        # ...
        while ls_rotten and num_of_fresh>0:
            num_rotten_curr_level = len(ls_rotten)
            for z in range(num_rotten_curr_level):
                # ... process and append neighbors ...
            t+=1 # Minute increments after processing a full layer
        
        if num_of_fresh > 0:
            return -1
        return max(0,t)
```
This is the standard BFS level-by-level time increment.
*   If `num_of_fresh` is initially 0, returns 0. Correct.
*   If `ls_rotten` is initially empty, but `num_of_fresh > 0`, loop condition `ls_rotten` is false. Loop doesn't run. `t` is 0. `num_of_fresh > 0` is true. Returns -1. Correct.
*   If oranges rot: `t` starts at 0. First minute passes, `t` becomes 1. Second minute passes, `t` becomes 2, etc. When the last orange rots, `num_of_fresh` becomes 0. The loop condition `num_of_fresh > 0` becomes false. The loop terminates. `t` holds the correct total minutes.
*   `max(0,t)`: Is redundant. If `fresh_oranges_count` is 0 initially, it returns 0. If it's `>0` and the loop runs, `t` will be `>0`. If `fresh_oranges_count > 0` but `ls_rotten` is empty (unreachable), `t` remains `0`, and it correctly returns -1. So `return t` would suffice.

The provided solution's Approach 3 is indeed clean and correct.

---

### 7. Key Insights and Patterns

1.  **BFS for Shortest Path/Minimum Time on Unweighted Graphs:** Whenever a problem asks for the "minimum number of steps," "shortest time," or "first occurrence" in a grid or graph where all movements/transitions have equal cost (e.g., 1 minute per step), BFS is almost always the optimal solution. It naturally explores layer by layer, guaranteeing the shortest path.
2.  **Multi-Source BFS:** If the "spreading" or "pathfinding" can start from multiple initial points (like multiple rotten oranges), initialize the BFS queue with *all* these starting points. They all spread simultaneously, and BFS correctly models this by processing them together in the first layer.
3.  **Level-by-Level Processing:** In BFS, to accurately count "minutes" or "levels," it's crucial to process all nodes at the current depth before moving to the next depth. This is achieved by:
    *   Getting the `len(queue)` at the beginning of each loop iteration.
    *   Dequing exactly that many elements before incrementing the level/minute counter.
4.  **State Modification for Visited/Processed Nodes:** For grid problems, modifying the grid in-place (e.g., changing `1` to `2`) is an efficient way to mark cells as "visited" or "processed" for the current BFS. This prevents redundant processing and cycles.
5.  **Counting Remaining Elements for Impossibility Check:** Maintain a counter for items that need to be "reached" or "processed" (like `num_of_fresh`). After the BFS completes, if this counter is not zero, it indicates that some elements were unreachable, leading to an "impossible" scenario.
6.  **Edge Case: No Initial Target Elements:** Always consider cases where the target count is zero at the start. For example, if there are no fresh oranges, the answer is 0 minutes.
7.  **Grid Traversal Helpers:** Using direction arrays (e.g., `[[1, 0], [0, 1], [-1, 0], [0, -1]]` for 4-directional) simplifies iterating through neighbors.
8.  **Python `collections.deque`:** For efficient queue operations (`append` and `popleft`), `collections.deque` is preferred over a standard Python list, especially for `pop(0)` which is O(N) for lists. While `m,n <= 10` makes `O(N)` list operations acceptable, `deque` is the best practice.