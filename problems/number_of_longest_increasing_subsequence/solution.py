class Solution:
    def findNumberOfLIS(self, nums):
        n = len(nums)
        lis = [0] * n
        fq = [0] * n
        lis[0] = 1
        fq[0] = 1
        lo = 1

        for i in range(1, len(nums)):
            mx = 0
            c = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    if lis[j] > mx:
                        mx = lis[j]
                        c = fq[j]
                    elif lis[j] == mx:
                        c += fq[j]
            fq[i] = c
            lis[i] = mx + 1
            if lo < lis[i]:
                lo = lis[i]

        count = 0
        for i in range(len(nums)):
            if lis[i] == lo:
                count += fq[i]

        return count