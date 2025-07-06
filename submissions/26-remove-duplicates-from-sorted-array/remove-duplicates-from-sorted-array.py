class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = [nums[i] for i in range(len(nums)) if (i==0 or nums[i]!=nums[i-1])]
        return len(nums)
        