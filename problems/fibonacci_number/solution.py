class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        j, k = 0, 1
        for i in range(2, n + 1):
            sums = k + j
            j = k
            k = sums
        return sums  

