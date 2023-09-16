class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.recursive_fib(n)

    def recursive_fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.recursive_fib(n - 1) + self.recursive_fib(n - 2)
# if i use this code without using cache, u can notice that the computing time and process is too high. so u can use cache as well








