class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelset=set(jewels)
        count=0
        for char in stones:
            if char in jewelset:
                count+=1
        return count        