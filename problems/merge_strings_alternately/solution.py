class Solution(object):
    def mergeAlternately(self, word1, word2):
        a=""
        max=len(word1)+len(word2)
        for i in range(0,max):
           if(i<len(word1)):
                a = a+word1[i]
           if(i<len(word2)):
                  a=a+word2[i]
        return a   