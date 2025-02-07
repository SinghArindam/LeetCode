class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # Initialize the current and maximum sum to the first element
        curr_sum = max_sum = nums[0]
        
        # Traverse the array starting from the second element
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_sum += nums[i]
            else:
                max_sum = max(max_sum, curr_sum)
                curr_sum = nums[i]
        # Final check in case the largest ascending subarray ends at the last element
        return max(max_sum, curr_sum)

        