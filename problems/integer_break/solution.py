class Solution:
    def integerBreak(self, no: int) -> int:
        if no <= 3:
            return no - 1
        answer = 1
        while no > 4:
            answer *= 3
            no -= 3
# This solution is awesome btw
        return answer * no