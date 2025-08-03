class Solution:
    def kthCharacter(self, k: int) -> str:
        if k == 1:
            return 'a'

        def transform(character: str) -> str:
            if character == 'z':
                return 'a'
            return chr(ord(character) + 1)

        midpoint = 1 << (k - 1).bit_length() - 1
        
        return transform(self.kthCharacter(k - midpoint))