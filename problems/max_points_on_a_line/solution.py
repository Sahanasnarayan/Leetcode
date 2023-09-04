class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 1
        n=len(points)
        res=2
        for i in range(0,n):
            slopecount = defaultdict(int)
            for j in range(0,n):
                if i!=j:
                    slope=atan2(points[i][1]-points[j][1],points[i][0]-points[j][0])
                    slopecount[slope]+=1
            for key,value in slopecount.items():
                res=max(res,value+1)
        return res                   
        