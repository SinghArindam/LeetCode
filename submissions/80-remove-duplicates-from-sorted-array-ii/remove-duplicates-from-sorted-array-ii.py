class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = [nums[i] for i in range(len(nums)) if (i<2) or (i>=2 and (nums[i]!=nums[i-1] or nums[i]!=nums[i-2]))]
        return len(nums)