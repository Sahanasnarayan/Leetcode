class Solution:
    def sortColors(self, nums: List[int]) -> None:
       i=j=k=ans=ans1=ans2=0
       while(i<len(nums)):
          if( nums[i]==0):
            ans=ans+1
            i+=1
          elif(nums[i]==1):
            ans1=ans1+1
            i+=1
          elif(nums[i]==2):
            ans2=ans2+1
            i+=1
       i=0        
       while(i<ans):
          nums[i]=0
          i+=1
    
       while(j<ans1):
          nums[i+j]=1
          j+=1
       j=j+i    
       while(k<ans2):
          nums[k+j]=2   
          k+=1