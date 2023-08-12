class Solution:
    def addDigits(self, num: int) -> int:
        while(num>=10):
            digits = [int(digit) for digit in str(num)]
            num = sum(digits)
        return num   
        
        #like divide the number by 10 and add it wuth the number 
