class Solution:
    def alternateDigitSum(self, n: int) -> int:
        num=str(n)
        asum=0
        for i in range(len(num)):
            if i % 2 == 0:
                asum += int(num[i])
            else:
                asum -= int(num[i])
        return asum