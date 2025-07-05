This document provides a comprehensive analysis of the LeetCode problem "Design a Number Container System," including its problem statement, various approaches, detailed logic explanation of the optimal solution, complexity analysis, edge case handling, and key insights.

---

## 1. Problem Summary

The problem asks us to design a `NumberContainers` class that can manage a system where numbers are stored at specific indices. The system must support two primary operations:

1.  **`change(int index, int number)`**: Assigns `number` to `index`. If `index` already has a number, it is replaced. This acts as both an insertion and an update operation.
2.  **`find(int number)`**: Returns the *smallest* `index` that currently holds the given `number`. If no `index` is filled with `number`, it should return `-1`.

**Constraints:**
*   `index` and `number` can be very large (`1` to `10^9`), implying that array-based storage indexed by `index` is not feasible due to memory limitations.
*   A maximum of `10^5` total calls will be made to `change` and `find`. This suggests that operations should ideally be logarithmic or constant time on average, rather than linear in the number of stored elements.

## 2. Explanation of Possible Approaches

We'll explore different approaches, from a naive solution to the most optimized one, highlighting their trade-offs.

### Approach 1: Naive / Brute-Force

**Data Structures:**
*   A single dictionary (hash map) to store `index -> number`. Let's call it `container`.

**Operations:**
*   **`NumberContainers()`**: Initialize `container = {}`.
*   **`change(index, number)`**: `container[index] = number`. This is `O(1)` on average.
*   **`find(number)`**: Iterate through all key-value pairs in `container`. For each pair `(idx, val)`, if `val == number`, keep track of the minimum `idx` found so far. Return the minimum `idx` or `-1` if no match.

**Complexity Analysis:**
*   **Time Complexity:**
    *   `change`: `O(1)` average.
    *   `find`: `O(M)` where `M` is the number of elements currently in the `container` (which can be up to `10^5`). In the worst case, `find` would iterate through all `10^5` entries. With `10^5` calls, this would be `O(M * N_find)` which is too slow (e.g., `10^5 * 10^5 = 10^{10}`).
*   **Space Complexity:** `O(M)` where `M` is the number of unique `index`es stored.

**Drawbacks:**
*   `find` operation is very inefficient.

### Approach 2: Using Two Dictionaries (Improved, but still not optimal)

To speed up `find`, we need to quickly get all indices for a given number.

**Data Structures:**
*   `self.index_to_number = {}`: Maps `index` to the `number` currently at that `index`. This helps with `change` (updating an existing `index`) and validation.
*   `self.number_to_indices = defaultdict(list)`: Maps `number` to a *list* of `index`es where that `number` is currently located.

**Operations:**
*   **`NumberContainers()`**: Initialize `self.index_to_number = {}` and `self.number_to_indices = defaultdict(list)`.
*   **`change(index, number)`**:
    1.  Get `old_number = self.index_to_number.get(index)`.
    2.  If `old_number` exists and `old_number != number`:
        *   Remove `index` from `self.number_to_indices[old_number]`. This requires iterating through the list, or using a more complex data structure for the list if elements need to be quickly removed.
    3.  `self.index_to_number[index] = number`.
    4.  Add `index` to `self.number_to_indices[number]`.
*   **`find(number)`**:
    1.  If `number` is not in `self.number_to_indices`, return `-1`.
    2.  Otherwise, get the list `indices = self.number_to_indices[number]`.
    3.  Find the minimum value in `indices`. This would involve sorting the list or iterating through it.

**Complexity Analysis:**
*   **Time Complexity:**
    *   `change`: If `self.number_to_indices[old_number]` is a simple list, removing `index` from it can be `O(K)` where `K` is the number of occurrences of `old_number`. Adding to a list is `O(1)`. Overall `O(K)`.
    *   `find`: Iterating through `indices` to find minimum is `O(K)`.
*   **Space Complexity:** `O(M)` where `M` is the total number of unique `index`es stored.

**Drawbacks:**
*   Both `change` (specifically removing the old index) and `find` can still be `O(K)`, where `K` can be up to `M` (total number of changes). This is not good enough.

### Approach 3: Optimized - Using Min-Heaps (The Provided Solution)

The key requirement for `find` is to get the *smallest* index. A min-heap (priority queue) is perfectly suited for this, as it allows `O(1)` access to the minimum element and `O(log K)` for insertions/deletions. The challenge is handling replacements efficiently.

**Core Idea:**
*   Maintain `index_to_number` for current state lookup.
*   Maintain `number_to_indices` where each value is a *min-heap* of indices.
*   For replacements (`change`), instead of eagerly removing the old `index` from its previous number's heap (which is slow for a generic heap), we use a **lazy deletion** strategy. When `find` is called, we peek at the top of the heap. If the `index` at the top no longer holds the `number` we are searching for (verified using `index_to_number`), it means that entry is stale. We pop it and repeat until we find a valid `index` or the heap is empty.

**Data Structures:**
*   `self.index_to_number = {}`: A dictionary mapping `index` to the `number` currently stored at that `index`. This is the single source of truth for the *current* state.
*   `self.num_to_indices = defaultdict(list)`: A dictionary mapping `number` to a list which is treated as a min-heap (using Python's `heapq` module) storing `index` values.

**Operations:**

#### `NumberContainers()`
```python
class NumberContainers:
    def __init__(self):
        # Stores the current number associated with each index.
        # Example: {2: 10, 1: 20} means index 2 has 10, index 1 has 20.
        self.index_to_number = {}
        
        # Stores a min-heap of indices for each number.
        # Example: {10: [1, 2, 3], 20: [5]} means 10 is at indices 1,2,3
        # (smallest first), and 20 is at index 5.
        # Using defaultdict(list) ensures an empty list (to be used as a heap)
        # is created automatically when a new number is accessed.
        self.num_to_indices = defaultdict(list)
```
*   **Purpose**: Initializes the two core data structures.
*   **Complexity**: `O(1)`.

#### `change(int index, int number)`
```python
import heapq # Needed for heap operations

class NumberContainers:
    # ... (init method) ...
    def change(self, index: int, number: int) -> None:
        # 1. Update the primary mapping: index -> current number
        # This records the new number at the given index, replacing any old one.
        # This is the "source of truth" for what number an index currently holds.
        self.index_to_number[index] = number
        
        # 2. Add the index to the min-heap for the new number.
        # This ensures that when we look up 'number', 'index' will be available.
        # heapq.heappush maintains the min-heap property.
        heapq.heappush(self.num_to_indices[number], index)
        
        # Note on lazy deletion: We DO NOT remove 'index' from the heap
        # of its OLD number here. This would be inefficient.
        # Instead, removal happens lazily during the 'find' operation.
```
*   **Logic**:
    1.  Updates `self.index_to_number[index]` to `number`. This is crucial because it immediately reflects the *current* state of `index`.
    2.  Pushes `index` onto the min-heap associated with `number` in `self.num_to_indices`.
    3.  **Lazy Deletion**: If `index` previously held a different number (`old_number`), the entry `index` is *not* removed from `self.num_to_indices[old_number]`'s heap. It remains there as a "stale" entry. This is acceptable because `find` will handle it.
*   **Time Complexity**: `O(log K)` where `K` is the number of elements in the heap for `number`. In the worst case, `K` can be up to `M` (total number of `change` operations). So, `O(log M)`.
*   **Space Complexity (per call):** `O(1)` for the operation itself, but contributes to overall `O(M)` storage.

#### `find(int number)`
```python
import heapq # Needed for heap operations
from collections import defaultdict # Needed for defaultdict

class NumberContainers:
    # ... (init and change methods) ...
    def find(self, number: int) -> int:
        # 1. Check if the number has any associated indices at all.
        if number not in self.num_to_indices:
            return -1
        
        # Get the min-heap for the requested number.
        heap = self.num_to_indices[number]
        
        # 2. Perform lazy removal:
        # Loop while the heap is not empty AND the smallest index in the heap (heap[0])
        # does NOT currently hold 'number' according to our primary 'index_to_number' map.
        # This condition means heap[0] is a "stale" entry that was previously associated
        # with 'number' but has since been reassigned to a different number.
        while heap and self.index_to_number.get(heap[0]) != number:
            # If it's stale, remove it from the heap.
            heapq.heappop(heap)
            
        # 3. Return the result:
        # If the heap is still not empty after removing all stale entries,
        # then heap[0] is the smallest VALID index for 'number'.
        # Otherwise, if the heap is empty, it means no valid index was found.
        return heap[0] if heap else -1

```
*   **Logic**:
    1.  Checks if `number` exists as a key in `self.num_to_indices`. If not, return `-1`.
    2.  Accesses the min-heap `heap` associated with `number`.
    3.  Enters a `while` loop for **lazy validation/deletion**:
        *   It continuously peeks at `heap[0]` (the smallest index in the heap).
        *   It then checks `self.index_to_number.get(heap[0])`. This is the *true* current number at that `index`.
        *   If `self.index_to_number.get(heap[0]) != number`, it means the `index` at `heap[0]` *used to* contain `number` when it was pushed onto the heap, but `change` was called on that `index` later, assigning it a different `number`. This makes the entry in the heap stale.
        *   `heapq.heappop(heap)` removes this stale entry. The loop continues until `heap[0]` *is* `number` (a valid entry) or the `heap` becomes empty.
    4.  If the heap is not empty after the loop, `heap[0]` is the smallest valid index. Otherwise, return `-1`.
*   **Time Complexity**:
    *   The cost of `find` is `O(log K)` for each `heappop` operation. While a single `find` call might perform multiple `heappop`s (in the worst case, `O(M)` of them if all entries in the heap are stale), the total number of `heappop`s across *all* `find` calls is bounded by the total number of `heappush` operations across *all* `change` calls. Each `index` can be pushed into a heap at most once per `change` call, and popped at most once due to being stale.
    *   Therefore, the **amortized time complexity** for `find` (and across all operations) is `O(log M)` for each individual `heappop`/`heappush` in a sequence of `M` operations.
    *   Considering `C` total calls (`C = M_change + N_find <= 10^5`): The total time complexity for all operations will be `O(C * log M)`. Since `M` can be up to `C`, this is `O(C log C)`. With `C = 10^5`, `log C` is about `17`. `10^5 * 17` operations is well within typical time limits.
*   **Space Complexity (per call):** `O(1)` for the operation itself, but relies on `O(M)` total space for the data structures.

## 4. Time and Space Complexity Analysis for Optimal Solution

*   **Time Complexity:**
    *   **`__init__`**: `O(1)`.
    *   **`change(index, number)`**: `O(log K)`, where `K` is the current number of elements in the heap for the given `number`. In the worst case, `K` can be up to the total number of `change` operations (`M`). So, `O(log M)`.
    *   **`find(number)`**: The cost for a single `find` operation depends on how many stale entries need to be popped. Each `heappop` takes `O(log K)`. However, each `index` is pushed into a heap at most once per `change` call, and it's popped at most once due to being stale. Therefore, over a sequence of `C` total operations (`M` `change` calls and `N` `find` calls, `C = M+N`), the total cost for all `heappush` and `heappop` operations combined is `O(C log M)`. This is an **amortized time complexity** of `O(log M)` per operation.
    *   **Overall**: Given `C <= 10^5`, the total time complexity is `O(C log C)`, which is efficient enough (`10^5 * log(10^5) approx 1.7 * 10^6` operations).

*   **Space Complexity:**
    *   `self.index_to_number`: Stores up to `M` unique `index`es, where `M` is the maximum number of `change` operations (and thus unique indices ever assigned). `O(M)`.
    *   `self.num_to_indices`: Each `index` is pushed into a heap at most once per `change` operation. Although some entries might be stale, they are eventually removed. The total number of `index`es across all heaps combined will not exceed `M`. `O(M)`.
    *   **Overall**: `O(M)` where `M` is the total number of `change` operations (`M <= 10^5`). This is efficient in terms of memory.

## 5. Edge Cases and How They Are Handled

*   **`find(number)` when `number` has never been inserted**:
    *   Handled by `if number not in self.num_to_indices: return -1;`. The `defaultdict` won't create an empty list unless `number` is accessed for insertion.
*   **`find(number)` when `number` was inserted but all its indices were later replaced with different numbers**:
    *   The `while heap and self.index_to_number.get(heap[0]) != number:` loop in `find` correctly handles this. It will pop all stale entries from the heap until the heap becomes empty. Then, `return heap[0] if heap else -1` will correctly return `-1`.
*   **`change(index, number)` where `index` previously held `number`**:
    *   `self.index_to_number[index] = number` just re-assigns the same value.
    *   `heapq.heappush(self.num_to_indices[number], index)` adds `index` to the heap again. This results in duplicate `index`es in the heap for the same `number`. This is acceptable because `find` will still eventually process the smallest valid `index`. For example, if `index` 5 is pushed for `number` 10, then 5 is changed to 20, then 5 is changed back to 10. The heap for 10 will contain `[5_old, ..., 5_new]`. When `find(10)` is called, `5_old` is encountered, `index_to_number.get(5_old)` is 20 (not 10), so `5_old` is popped. Then `5_new` is encountered, `index_to_number.get(5_new)` is 10, so `5_new` is returned.
*   **Large `index` and `number` values (up to `10^9`)**:
    *   Using dictionaries (`self.index_to_number`, `self.num_to_indices`) is perfect for this. They handle sparse keys efficiently without requiring a large pre-allocated array. Hash map keys can be any hashable object, including large integers.
*   **Constraints on total calls (10^5)**:
    *   The amortized `O(log M)` time complexity per operation (leading to `O(C log C)` total) is designed to meet this constraint, where `C` is the total number of calls.

## 6. Clean, Well-Commented Version of the Optimal Solution

```python
from collections import defaultdict
import heapq

class NumberContainers:
    """
    Initializes a NumberContainer system.
    This system efficiently stores numbers at given indices and allows
    retrieval of the smallest index for a specific number.
    """
    def __init__(self):
        # self.index_to_number: A dictionary mapping an index to the
        #                       number currently stored at that index.
        # This acts as the primary source of truth for the current state
        # of each container.
        # Example: {2: 10, 1: 20} means index 2 holds 10, index 1 holds 20.
        self.index_to_number = {}

        # self.num_to_indices: A dictionary mapping a number to a min-heap
        #                     (priority queue) of indices where that number is present.
        # Using defaultdict(list) ensures that if a number is accessed for the
        # first time, an empty list (which will become a heap) is automatically created.
        # Example: {10: [1, 2, 3], 20: [5]} means number 10 is found at indices
        # 1, 2, and 3 (smallest first), and number 20 at index 5.
        # This structure allows O(1) access to the smallest index and O(log K)
        # for adding new indices, where K is the number of indices for that number.
        self.num_to_indices = defaultdict(list)
    
    def change(self, index: int, number: int) -> None:
        """
        Fills the container at 'index' with 'number'.
        If there's already a number at 'index', it's replaced.
        
        Args:
            index (int): The index of the container to modify.
            number (int): The number to place in the container at 'index'.
        """
        # 1. Update the primary mapping for the given index.
        # This step is crucial as it reflects the most current value at 'index'.
        self.index_to_number[index] = number
        
        # 2. Push the 'index' onto the min-heap associated with the 'number'.
        # This heap will keep track of all indices where 'number' has been placed.
        # Note: If 'index' was previously associated with a different number,
        # it is NOT removed from that old number's heap here. This is part of
        # the "lazy deletion" strategy to keep 'change' fast (O(log K)).
        heapq.heappush(self.num_to_indices[number], index)
    
    def find(self, number: int) -> int:
        """
        Returns the smallest index for the given 'number',
        or -1 if no index is currently filled by 'number'.
        
        Args:
            number (int): The number to search for.
            
        Returns:
            int: The smallest index where 'number' is found, or -1.
        """
        # 1. Check if the 'number' exists as a key in our num_to_indices map.
        # If not, it means this number has never been assigned to any index,
        # or all its assigned indices have been replaced and lazily cleared.
        if number not in self.num_to_indices:
            return -1
        
        # Get the min-heap of indices associated with this 'number'.
        heap = self.num_to_indices[number]
        
        # 2. Perform lazy validation and removal of stale entries from the heap.
        # The loop continues as long as the heap is not empty AND
        # the number currently at the smallest index in the heap (heap[0])
        # does NOT match the 'number' we are searching for.
        # This condition signifies that heap[0] is a "stale" entry:
        # it was once associated with 'number', but 'index_to_number[heap[0]]'
        # has since been updated to a different value.
        while heap and self.index_to_number.get(heap[0]) != number:
            # If the entry is stale, remove it from the heap.
            # heapq.heappop maintains the min-heap property.
            heapq.heappop(heap)
        
        # 3. Return the result.
        # After the loop, if the heap is not empty, its smallest element (heap[0])
        # is guaranteed to be a valid index for 'number'.
        # If the heap is empty, it means all indices for 'number' have been replaced
        # or no such index ever existed.
        return heap[0] if heap else -1

```

## 7. Key Insights and Patterns

*   **Design for Specific Operations**: The problem's constraints dictate the choice of data structures. The need for `O(1)` or `O(log K)` `find_min` directly points to a min-heap.
*   **Hash Maps for Sparse Data and Efficient Lookups**: When `index` and `number` values can be very large (`10^9`), traditional arrays are not feasible due to memory. Hash maps (`dict` in Python) are ideal for mapping arbitrary keys to values with `O(1)` average-case time complexity.
*   **Min-Heaps (Priority Queues) for Smallest/Largest Element Retrieval**: When the problem specifically asks for the "smallest" or "largest" element among a dynamic set, a min-heap (or max-heap) is the go-to data structure. It offers `O(1)` access to the extremum and `O(log K)` for insertions and deletions (if the heap supports arbitrary deletions, which standard `heapq` doesn't directly).
*   **Lazy Deletion/Invalidation Pattern**: This is the most crucial pattern in this solution. When a data structure (like Python's `heapq` which doesn't efficiently support arbitrary removal by value) cannot easily remove elements that become invalid, a common strategy is "lazy deletion."
    *   Instead of immediately removing an invalid item, you leave it in the data structure.
    *   During retrieval, you check if the item is still valid using a secondary source of truth (here, `self.index_to_number`).
    *   If invalid, you discard it (pop it from the heap) and continue until a valid item is found or the data structure is exhausted.
    *   This pattern amortizes the cost of deletion across multiple retrieval operations, often leading to better overall performance if reads are less frequent or if many invalid items can be processed in a single pass. It saves time during the `change` operation by deferring the costly removal.
*   **Amortized Analysis**: Understanding that while a single `find` operation might appear costly (multiple pops), the total cost over a sequence of operations is efficient because each element is popped at most once due to being stale. This is a common analysis technique for algorithms with varying costs per operation.
*   **Trade-offs**: The lazy deletion approach trades slightly increased space (for potentially stale entries in heaps) and potentially higher worst-case *single-operation* `find` time for significantly simpler and faster `change` operations, resulting in excellent *amortized* performance for both.