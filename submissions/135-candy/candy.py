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
        # if not ratings:
        #     return 0
        # total_candies = 1
        # up_slope_len = 0
        # down_slope_len = 0
        # peak_len = 0
        # for i in range(1, len(ratings)):
        #     if ratings[i] > ratings[i - 1]:
        #         up_slope_len += 1
        #         down_slope_len = 0
        #         peak_len = up_slope_len
        #         total_candies += 1 + up_slope_len
        #     elif ratings[i] == ratings[i - 1]:
        #         up_slope_len = down_slope_len = peak_len = 0
        #         total_candies += 1
        #     else:
        #         up_slope_len = 0
        #         down_slope_len += 1
        #         total_candies += down_slope_len
        #         if peak_len < down_slope_len:
        #             total_candies += 1    
        # return total_candies

        # Approach 4
        # num_kids = len(ratings)
        # candies = [0] * num_kids
        # queue = deque()
        # for i in range(num_kids):
        #     is_left_valley = (i == 0) or (ratings[i] <= ratings[i-1])
        #     is_right_valley = (i == num_kids - 1) or (ratings[i] <= ratings[i+1])
        #     if is_left_valley and is_right_valley:
        #         candies[i] = 1
        #         queue.append(i)
        # while queue:
        #     kid_index = queue.popleft()
        #     if kid_index > 0:
        #         neighbor_index = kid_index - 1
        #         if ratings[neighbor_index] > ratings[kid_index] and candies[neighbor_index] < candies[kid_index] + 1:
        #             candies[neighbor_index] = candies[kid_index] + 1
        #             queue.append(neighbor_index)
        #     if kid_index < num_kids - 1:
        #         neighbor_index = kid_index + 1
        #         if ratings[neighbor_index] > ratings[kid_index] and candies[neighbor_index] < candies[kid_index] + 1:
        #             candies[neighbor_index] = candies[kid_index] + 1
        #             queue.append(neighbor_index)
        # return sum(candies)

        # Approach 5
        # num_kids = len(ratings)
        # candies = [1] * num_kids
        # sorted_kids = sorted(range(num_kids), key=lambda k: ratings[k])
        # for i in sorted_kids:
        #     if i > 0 and ratings[i] > ratings[i - 1]:
        #         candies[i] = max(candies[i], candies[i - 1] + 1)
        #     if i < num_kids - 1 and ratings[i] > ratings[i + 1]:
        #         candies[i] = max(candies[i], candies[i + 1] + 1)
        # return sum(candies)

        # Approach 6
        # import sys
        sys.setrecursionlimit(2 * 10**4 + 5)
        num_kids = len(ratings)
        memo_left = {}
        memo_right = {}
        def get_left_candies(i):
            if i in memo_left:
                return memo_left[i]
            if i > 0 and ratings[i] > ratings[i - 1]:
                res = 1 + get_left_candies(i - 1)
            else:
                res = 1
            memo_left[i] = res
            return res
        def get_right_candies(i):
            if i in memo_right:
                return memo_right[i]
            if i < num_kids - 1 and ratings[i] > ratings[i + 1]:
                res = 1 + get_right_candies(i + 1)
            else:
                res = 1
            memo_right[i] = res
            return res
        total_candies = 0
        for i in range(num_kids):
            total_candies += max(get_left_candies(i), get_right_candies(i))
        return total_candies