class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s_list = list(s)
        #using 2 pointers and recursion
        def makePalindrome(s: list, i: int, j: int) -> str:
            if i >= j:
                return ''.join(s)
            
            if s[i] > s[j]:
                s[i] = s[j]
            elif s[i] < s[j]:
                s[i] = min(s[i], s[j])
                s[j] = s[i]
            
            return makePalindrome(s, i + 1, j - 1)
        
        return makePalindrome(s_list, 0, len(s_list) - 1)

                     