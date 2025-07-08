import bisect
import functools

class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        events.sort()
        n = len(events)
        @functools.lru_cache(None)
        def dp(i: int, count: int) -> int:
            if count == 0 or i == n:
                return 0
            skip_current_event_value = dp(i + 1, count)
            current_event_value = events[i][2]
            current_event_end_day = events[i][1]
            next_event_idx = bisect.bisect_right(events, [current_event_end_day, float('inf'), float('inf')], lo=i + 1)
            
            attend_current_event_value = current_event_value + dp(next_event_idx, count - 1)

            # Store the result in memoization table and return the maximum of the two options.
            return max(skip_current_event_value, attend_current_event_value)

        # Start the DP process from the first event (index 0) with k allowed events.
        return dp(0, k)