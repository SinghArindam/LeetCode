class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority_element = None

        for num in nums:
            if count == 0:
                majority_element = num
                count = 1
            elif num == majority_element:
                count += 1
            else:
                count -= 1
                
        return majority_element
        