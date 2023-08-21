class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=0
        ans=""
        carry=0
        while(i<len(a) or i<len(b) or carry!=0):
            x=0
            if(i<len(a) and a[len(a)-i-1]=='1'):
                x=1
            y=0
            if(i<len(b) and b[len(b)-i-1]=='1'):
                y=1
            ans=str((x+y+carry)%2)+ans
            carry=(x+y+carry)//2
            i+=1
        return ans
        