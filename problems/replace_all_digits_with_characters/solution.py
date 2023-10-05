class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(char, num):
            return chr(ord(char) + int(num))
        stack = []
        for char in s:
            if char.isdigit():
                stack[-1] += shift(stack[-1], char)
            else:
                stack.append(char)

        return "".join(stack)