class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans=0
        if low%2==1 or high%2==1:
            ans=((high-low)//2) +1
        else:
            ans=(high-low)//2
        return ans          