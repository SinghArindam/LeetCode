Here's a set of atomic notes for LeetCode problem 2456, "Construct Smallest Number From DI String", suitable for spaced repetition:

- **Concept**: Problem Goal - Construct Lexicographically Smallest Number
  **Context**: Given a `pattern` string of 'I' (increasing) and 'D' (decreasing), construct a `num` string of length `n+1` that satisfies the specified digit relationships. The final `num` must be the lexicographically smallest possible.
  **Example**: `pattern = "IIIDIDDD"` -> `num = "123549876"`

- **Concept**: Digit Constraints
  **Context**: The `num` string must consist of unique digits from '1' through '9', each used at most once. The problem constraint `pattern.length <= 8` means `num` has a max length of 9, perfectly aligning with using '1' through '9' exactly once.
  **Example**: `pattern.length = 8` implies `num` length 9, uses `1,2,3,4,5,6,7,8,9` uniquely.

- **Concept**: Optimal Approach - Greedy with Stack
  **Context**: The most efficient and straightforward solution employs a greedy strategy combined with a stack to process the pattern and build the lexicographically smallest `num`.
  **Example**: The algorithm iterates through potential digits, pushing them onto a stack and "flushing" them when conditions allow.

- **Concept**: Iteration Range for Digits
  **Context**: The main loop runs `n+1` times (from `i=0` up to `pattern.size()`) to cover all `n+1` digits required for the `num` string, as `num` is one digit longer than `pattern`.
  **Example**: For `pattern.length = 3` (`"DDD"`), the loop runs for `i = 0, 1, 2, 3`, effectively considering digits `1, 2, 3, 4`.

- **Concept**: Candidate Digit Generation (`i+1`)
  **Context**: In each iteration `i`, the integer `i+1` is pushed onto the stack. These are the smallest available unique digits (starting from '1') that are candidates for placement in `num`.
  **Example**: `stk.push(i+1)` ensures digits are considered in increasing order (1, then 2, then 3, etc.).

- **Concept**: Stack's Role for Decreasing Sequences ('D')
  **Context**: The stack's Last-In, First-Out (LIFO) property is crucial for 'D' (decreasing) patterns. Digits pushed onto the stack in increasing order (e.g., `[1, 2, 3]`) are popped in decreasing order (e.g., `3, 2, 1`), naturally satisfying `num[i] > num[i+1]`.
  **Example**: If `pattern` segment is `DDD`, numbers pushed `1,2,3,4` are popped as `4,3,2,1` (e.g., `num[0]=4, num[1]=3, num[2]=2, num[3]=1`).

- **Concept**: 'I' Character as a Delimiter (Flush Point)
  **Context**: An 'I' character (`pattern[i] == 'I'`) indicates an increasing relationship (`num[i] < num[i+1]`). It also acts as a boundary, signaling that any accumulated digits (typically from a preceding 'D' sequence) in the stack must now be resolved and appended to the `result` string.
  **Example**: In `...DDI`, the 'I' causes the digits corresponding to the `DD` part to be popped and committed.

- **Concept**: End of Pattern as a Delimiter
  **Context**: The loop's final iteration (when `i == pattern.size()`) acts as a mandatory flush point. Any digits remaining in the stack at this stage must be popped and appended to complete the `num` string.
  **Example**: For `pattern="DDD"`, the final digit `4` is pushed at `i=3`, and because `i == pattern.size()` is true, the entire stack `[1,2,3,4]` is popped.

- **Concept**: Commitment Strategy
  **Context**: Digits are held in the stack and only "committed" (popped and appended to `result`) when an 'I' character is encountered or the end of the `pattern` is reached. This strategic timing ensures correct ordering for both 'I' and 'D' constraints.
  **Example**: For `IIIDIDDD`, `1,2,3` are popped immediately for 'III', but `4,5` are processed together for `DI`.

- **Concept**: Lexicographical Smallest Guarantee (Greedy Principle)
  **Context**: The solution ensures lexicographical minimality by always attempting to use the smallest available digit (`i+1`) and by only committing these digits to the result string when strictly necessary (at 'I' boundaries or end of pattern). This ensures the smallest possible block of numbers is used for decreasing sequences.
  **Example**: For `DDD`, it correctly uses `4,3,2,1` instead of `9,8,7,6` because `4,3,2,1` is the smallest set of four unique digits that can form a decreasing sequence.

- **Concept**: Time Complexity (Optimal Solution)
  **Context**: The algorithm iterates through the `pattern` once. Each digit (from `1` to `N+1`) is pushed onto the stack exactly once and popped exactly once. Stack operations are O(1).
  **Example**: `O(N)` where `N` is `pattern.length`.

- **Concept**: Space Complexity (Optimal Solution)
  **Context**: The stack can temporarily hold up to `N+1` elements (in the worst case, e.g., if the pattern is all 'D's), and the `result` string grows to length `N+1`.
  **Example**: `O(N)` where `N` is `pattern.length`.

- **Concept**: Handling Smallest Pattern Length (`N=1`)
  **Context**: The algorithm correctly processes single-character patterns due to the `i <= pattern.size()` loop condition and the stack's logic.
  **Example**: `pattern="I"` results in "12"; `pattern="D"` results in "21".

- **Concept**: Handling All Increasing Patterns (`"II...I"`)
  **Context**: If the pattern consists only of 'I's, each digit pushed onto the stack is immediately popped and appended to the result, naturally forming an increasing sequence.
  **Example**: `pattern="IIII"` correctly yields "12345".

- **Concept**: Handling All Decreasing Patterns (`"DD...D"`)
  **Context**: If the pattern consists only of 'D's, all digits (`1` through `N+1`) are pushed onto the stack. They are then popped in reverse order only when the end of the pattern is reached.
  **Example**: `pattern="DDD"` correctly yields "4321".

- **Concept**: General Principle of Lexicographical Smallest
  **Context**: A fundamental strategy for lexicographical minimality is to always try to place the smallest possible available characters/digits at the earliest possible positions.
  **Example**: This problem's solution embodies this by generating candidate digits `1, 2, 3...` and strategically deciding their placement.

- **Concept**: Stack for Reordering/Reversal
  **Context**: The LIFO property of a stack is a powerful tool for problems where elements need to be processed or output in an order reverse to their accumulation.
  **Example**: Converting an incrementally built sequence (`1,2,3`) into a decremental output (`3,2,1`) for 'D' segments.

- **Concept**: Delimiter-Driven Processing
  **Context**: This problem showcases a common algorithmic pattern where a specific condition or character (a "delimiter") triggers the processing or "flushing" of accumulated data.
  **Example**: The 'I' character and the end of the pattern string act as delimiters for committing digits from the stack.