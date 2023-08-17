class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
       
    
        low=max(weights)
        high=sum(weights)
        
        while(low<high):
            mid=low+(high-low)//2
            if self.isweight(mid,weights,days):
                high=mid
            else:
                low=mid+1
        return low  
    def isweight(self,capacity,weights,days):
        dayspassed=1
        totalweight=0
        for weight in weights:
            totalweight+=weight
            if totalweight>capacity:
                totalweight=weight
                dayspassed+=1
                if dayspassed>days:
                    return False
        return True  
        #didnt understand this sum better                    