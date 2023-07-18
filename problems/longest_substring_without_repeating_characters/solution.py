class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        maxl = 0
        Set = set()
        l = 0      
        for r in range(length):
            if s[r] not in Set:
                Set.add(s[r])
                maxl = max(maxl, r - l + 1)
            else:
                while s[r] in Set:
                    Set.remove(s[l])
                    l += 1
                Set.add(s[r])       
        return maxl