class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            stack.pop() if char == '*' else stack.append(char)
        return ''.join(stack)