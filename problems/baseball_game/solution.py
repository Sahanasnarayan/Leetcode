class Solution:
    def calPoints(self, o: List[str]) -> int:
        ans=[]
        for i in o:
            if i=='x':
                ans.append(x)
            elif i=='+':
                ans.append(ans[-1]+ans[-2]) 
            elif i=='D':
                ans.append(2*ans[-1])
            elif i=='C':
                ans.pop()
            else:
                ans.append(int(i))
        return sum(ans)                   