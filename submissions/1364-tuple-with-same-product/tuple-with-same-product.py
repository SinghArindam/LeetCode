from collections import defaultdict
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # Create a dictionary to count the frequency of each product from a pair.
        count = defaultdict(int)
        n = len(nums)
        # Iterate over all unique pairs (i, j) with i < j.
        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                count[prod] += 1

        result = 0
        # For each product that occurs 'v' times, the number of tuples that can be formed is:
        # C(v, 2) * 8 = (v * (v - 1) // 2) * 8.
        for v in count.values():
            result += v * (v - 1) // 2

        return result * 8
