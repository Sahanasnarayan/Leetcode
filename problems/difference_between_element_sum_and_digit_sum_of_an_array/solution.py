class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        a=sum(nums)
        ssum=0
        for num in nums:
            if(num>=10):
                numstr=str(num)
                for char in numstr:
                    ssum+=int(char)
            else: ssum+=num
        if ssum>a:
            return ssum-a
        else:
            return a-ssum               
                