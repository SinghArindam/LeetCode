class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # If strings are already equal, no swap is needed.
        if s1 == s2:
            return True
        
        # Collect all mismatched pairs.
        diff = [(a, b) for a, b in zip(s1, s2) if a != b]
        
        # A valid one-swap fix is only possible if there are exactly two differences
        # and swapping the mismatched characters in one string makes the strings equal.
        return len(diff) == 2 and diff[0] == diff[1][::-1]
