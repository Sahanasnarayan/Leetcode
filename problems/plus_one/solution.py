class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        while(i>=0):
            if(digits[i]==9):
               digits[i]= 0
               i-=1
            else:    
               digits[i]=digits[i]+1
               return digits
        digits.append(0)
        digits[0]=1
        return digits    