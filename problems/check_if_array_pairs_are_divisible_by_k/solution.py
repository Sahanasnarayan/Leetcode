class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        remainder_freq = [0] * k
        
        for num in arr:
            remainder = num % k
            remainder_freq[remainder] += 1
        
        if remainder_freq[0] % 2 != 0:
            return False
        
        for i in range(1, k // 2 + 1):
            if remainder_freq[i] != remainder_freq[k - i]:
                return False
        
        return True
        