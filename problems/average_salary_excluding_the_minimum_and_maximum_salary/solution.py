class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sum=0
        for num in range(1,len(salary)-1):
            sum+=salary[num]
        return (sum/(len(salary)-2))    