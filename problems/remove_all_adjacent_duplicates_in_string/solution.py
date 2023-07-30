class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for i in s:
            if stack and i == stack[-1]: #this line is very important
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)