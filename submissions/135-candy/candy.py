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
        # num_kids = len(ratings)
        # left_to_right = [1] * num_kids
        # right_to_left = [1] * num_kids
        # for i in range(1, num_kids):
        #     if ratings[i] > ratings[i - 1]:
        #         left_to_right[i] = left_to_right[i - 1] + 1
        # for i in range(num_kids - 2, -1, -1):
        #     if ratings[i] > ratings[i + 1]:
        #         right_to_left[i] = right_to_left[i + 1] + 1
        # total_candies = 0
        # for i in range(num_kids):
        #     total_candies += max(left_to_right[i], right_to_left[i])
        # return total_candies
        
        # Approach 3
        if not ratings:
            return 0
        total_candies = 1
        up_slope_len = 0
        down_slope_len = 0
        peak_len = 0
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                up_slope_len += 1
                down_slope_len = 0
                peak_len = up_slope_len
                total_candies += 1 + up_slope_len
            elif ratings[i] == ratings[i - 1]:
                up_slope_len = down_slope_len = peak_len = 0
                total_candies += 1
            else:
                up_slope_len = 0
                down_slope_len += 1
                total_candies += down_slope_len
                if peak_len < down_slope_len:
                    total_candies += 1    
        return total_candies