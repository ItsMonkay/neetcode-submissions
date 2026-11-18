class Solution:
    def hammingWeight(self, n: int) -> int:
        ham = 0

        while n > 0:
            ham += n%2
            n = n >> 1
        

        return ham

        