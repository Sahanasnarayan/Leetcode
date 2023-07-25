class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr=sorted(arr)
        l=0
        r=1
        while(r<len(arr)-1):
            if(arr[r]-arr[l])!=(arr[r+1]-arr[l+1]):
                return False
            l+=1
            r+=1
        return True        