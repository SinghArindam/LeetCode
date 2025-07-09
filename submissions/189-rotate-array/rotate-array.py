class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k>len(nums):
            k -= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        # new_nums = []
        # if k>=len(nums):
        #     return
        # for i in range(len(nums)):
        #     new_nums.append(nums[i-k])
        # nums[:] = new_nums

        