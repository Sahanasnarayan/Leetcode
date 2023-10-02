class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n=len(colors)
        A=0
        B=0
        for i in range(0,n-2):
            if(colors[i]==colors[i+1] and colors[i+1] == colors[i+2] and colors[i]=='A'):
                 A+=1
            if(colors[i]==colors[i+1] and colors[i+1] == colors[i+2] and colors[i]=='B'):
                 B+=1
        if(B>=A):
             return False
        return True
        