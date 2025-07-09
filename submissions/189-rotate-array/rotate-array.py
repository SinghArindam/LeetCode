class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k>len(nums):
            k -= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

        