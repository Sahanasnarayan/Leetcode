class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        a=[]
        for element in nums:
            sum=sum+element
            a.append(sum)
        return a    