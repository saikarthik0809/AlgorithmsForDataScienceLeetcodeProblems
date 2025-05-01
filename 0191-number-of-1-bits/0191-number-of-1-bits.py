class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()  # direct formula to give Hamming wt in python.
        