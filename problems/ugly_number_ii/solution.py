class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return 0

        ugly_numbers = [1]
        p2, p3, p5 = 0, 0, 0  # Pointers for multiples of 2, 3, and 5

        while len(ugly_numbers) < n:
        # Calculate the next ugly number as the minimum of the products
            next_ugly = min(ugly_numbers[p2] * 2, ugly_numbers[p3] * 3, ugly_numbers[p5] * 5)

        # Update pointers for multiples of 2, 3, and 5
            if next_ugly == ugly_numbers[p2] * 2:
                p2 += 1
            if next_ugly == ugly_numbers[p3] * 3:
                p3 += 1
            if next_ugly == ugly_numbers[p5] * 5:
                p5 += 1

            ugly_numbers.append(next_ugly)

        return ugly_numbers[-1]
        