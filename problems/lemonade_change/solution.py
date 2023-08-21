class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bank = {5: 0, 10: 0}  
        
        for num in bills:
            if num == 5:
                bank[5] += 1
            elif num == 10:
                if bank[5] >= 1:
                    bank[5] -= 1
                    bank[10] += 1
                else:
                    return False
            elif num == 20:
                if bank[10] >= 1 and bank[5] >= 1:
                    bank[10] -= 1
                    bank[5] -= 1
                elif bank[5] >= 3:
                    bank[5] -= 3
                else:
                    return False
                
        return True     
