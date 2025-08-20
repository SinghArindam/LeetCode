class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Approach 1
        # num_kids = len(ratings)
        # candies = [1] * num_kids
        # for i in range(1, num_kids):
        #     if ratings[i] > ratings[i - 1]:
        #         candies[i] = candies[i - 1] + 1
        # for i in range(num_kids - 2, -1, -1):
        #     if ratings[i] > ratings[i + 1]:
        #         candies[i] = max(candies[i], candies[i + 1] + 1)
        # return sum(candies)

        # Approach 2
        num_kids = len(ratings)
        left_to_right = [1] * num_kids
        right_to_left = [1] * num_kids
        for i in range(1, num_kids):
            if ratings[i] > ratings[i - 1]:
                left_to_right[i] = left_to_right[i - 1] + 1
        for i in range(num_kids - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right_to_left[i] = right_to_left[i + 1] + 1
        total_candies = 0
        for i in range(num_kids):
            total_candies += max(left_to_right[i], right_to_left[i])
        return total_candies
        