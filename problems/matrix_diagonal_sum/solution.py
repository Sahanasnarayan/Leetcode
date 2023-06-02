class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
       sum=0
       n = len(mat)
       for i in range(n):
            sum =sum + mat[i][i] 
            sum= sum + mat[i][n-i-1]
            
       if n%2==1 :
            sum = sum - mat[n//2][n//2]
       return sum