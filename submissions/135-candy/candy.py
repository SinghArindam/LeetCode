class Solution:
    def candy(self, ratings: List[int]) -> int:
        num_kids = len(ratings)
        candies = [1] * num_kids
        for i in range(1, num_kids):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(num_kids - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)
        