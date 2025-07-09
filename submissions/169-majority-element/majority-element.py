class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            if num not in d.keys():
                d[num] = nums.count(num)
        majority_element = max(d, key=d.get)
        return majority_element
        