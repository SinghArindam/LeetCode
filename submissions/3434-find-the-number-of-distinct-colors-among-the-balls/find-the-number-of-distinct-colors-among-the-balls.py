class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # ball_to_color stores the current color for each ball updated so far.
        ball_to_color = {}
        # color_freq stores the count of balls for each color.
        color_freq = {}
        result = []
        
        for ball, color in queries:
            # If the ball is already colored:
            if ball in ball_to_color:
                prev_color = ball_to_color[ball]
                # If the color is the same, no change is needed.
                if prev_color == color:
                    result.append(len(color_freq))
                    continue
                # Decrement the count for the previous color.
                color_freq[prev_color] -= 1
                if color_freq[prev_color] == 0:
                    del color_freq[prev_color]
            
            # Update the ball's color.
            ball_to_color[ball] = color
            color_freq[color] = color_freq.get(color, 0) + 1
            
            # The distinct colors count is the number of keys in color_freq.
            result.append(len(color_freq))
        
        return result
