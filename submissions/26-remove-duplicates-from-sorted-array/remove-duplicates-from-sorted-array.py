class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_nums = []
        # for i in range(len(nums)):
        #     if nums[i]!=nums[i-1]:
        #         print(nums[i])
        #         new_nums.append(nums[i])
        #     else:
        #         continue
        new_nums = [nums[i] for i in range(len(nums)) if (i==0 or nums[i]!=nums[i-1])]
        nums[:] = new_nums
        return len(new_nums)
        