class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        bad_pairs = 0
        count = {}
        # Process each index and number in nums
        for i, num in enumerate(nums):
            key = i - num
            # For index i, there are i pairs with previous indices.
            # Among these, count[key] pairs are good, so the rest are bad.
            bad_pairs += i - count.get(key, 0)
            count[key] = count.get(key, 0) + 1
        return bad_pairs

        