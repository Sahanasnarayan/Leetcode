class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
           return x 
            
        left = 1
        right = x // 2

        while left <= right:
           mid = (left + right) // 2

           if mid * mid == x:
              return mid

           if mid * mid < x:
              left = mid + 1
              result = mid
           else:
              right = mid - 1

        return result
        