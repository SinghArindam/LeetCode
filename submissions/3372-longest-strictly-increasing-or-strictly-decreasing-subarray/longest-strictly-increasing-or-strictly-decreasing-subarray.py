class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # For a single element, the longest subarray is 1.
        n = len(nums)
        if n == 0:
            return 0
        
        # Initialize both counters to 1 (each element is a subarray of length 1)
        inc = 1
        dec = 1
        ans = 1
        
        for i in range(1, n):
            # Check for strictly increasing sequence
            if nums[i] > nums[i - 1]:
                inc += 1
            else:
                inc = 1
            
            # Check for strictly decreasing sequence
            if nums[i] < nums[i - 1]:
                dec += 1
            else:
                dec = 1
            
            # Update the answer with the maximum length found so far
            ans = max(ans, inc, dec)
        
        return ans

        