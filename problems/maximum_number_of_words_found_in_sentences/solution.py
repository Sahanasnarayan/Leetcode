class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        lengths = [] 
        for sentence in sentences: 
            word_count = sentence.count(" ") + 1  
            lengths.append(word_count)
        return max(lengths)