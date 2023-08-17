
class Solution:
    def maxDistance(self, pos: List[int], balls: int) -> int:
       pos.sort()
       n=len(pos)
       low=1
       high=pos[n-1]-pos[0]
       while(low<=high):
           mid=low+(high-low)//2
           if self.isfeasible(mid,pos,balls):
               ans=mid
               low=mid+1
           else:
               high=mid-1
       return ans
    def isfeasible(self,min_dis,pos,balls):
        ballplaced=1
        previndex=0
        for i in range(1,len(pos)):
            if pos[i]-pos[previndex]>=min_dis:
                 ballplaced+=1
                 previndex=i
                 if ballplaced==balls:
                     return True
        return ballplaced>=balls                             
