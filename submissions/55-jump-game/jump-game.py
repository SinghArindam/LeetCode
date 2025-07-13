class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest_reach = 0
        for i in range(n):
            if i > farthest_reach:
                return False
            farthest_reach = max(farthest_reach, i + nums[i])
            if farthest_reach >= n - 1:
                return True
        return True