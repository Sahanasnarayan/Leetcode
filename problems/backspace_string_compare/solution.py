class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:   
        
        def buildstring(s):    
            stack=[]
            for char in s:
                if char == '#':
                    if stack:
                       stack.pop()
                else:
                    stack.append(char)
            return ''.join(stack)
        return buildstring(s) == buildstring(t)