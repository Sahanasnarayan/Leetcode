class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[]
        slate=[]
        self.helper(s,0,slate,res)
        return res
    def helper(self,s,index,slate,res):
        if(index==len(s)):
            res.append(''.join(slate))
            return
        if s[index].isdigit()==True:
            slate.append(s[index])
            self.helper(s,index+1,slate,res)
            slate.pop()
        else:
            slate.append(s[index].lower())
            self.helper(s,index+1,slate,res)
            slate.pop()
            slate.append(s[index].upper())
            self.helper(s,index+1,slate,res)
            slate.pop()        
#even the pythontutor visualizer is complicated. just remember this was based on recursion