class Solution:
    def reverseWords(self, s: str) -> str:
        s = ' '.join(s.split())
        words = s.split()
        words.reverse()
        return ' '.join(words)
                

