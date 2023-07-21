class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2=''
        for i in s:
            if i.isalnum() :
                s2 += i
            s2 = s2.lower()
        if s2 == s2[::-1]:
            return True
        else:
            return False            