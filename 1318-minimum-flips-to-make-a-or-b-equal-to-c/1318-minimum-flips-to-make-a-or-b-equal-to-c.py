class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        flips = 0
        
        while a > 0 or b > 0 or c > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1
            
            if bit_c == 0:
                # Both bits must be flipped to 0 if they are 1
                flips += (bit_a + bit_b)
            else:
                # At least one bit must be 1. If both are 0, we need 1 flip.
                if bit_a == 0 and bit_b == 0:
                    flips += 1
            
            # Shift right to process the next bit
            a >>= 1
            b >>= 1
            c >>= 1
            
        return flips