class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Slow-runner pointer
        for j in range(len(nums)):
            if nums[j] != val:
                nums[k] = nums[j]
                k += 1
        return k