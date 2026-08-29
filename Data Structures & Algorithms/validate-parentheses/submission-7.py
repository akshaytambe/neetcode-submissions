class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for i, char in enumerate(s):
            if char in ("(", "{", "["):
                stack.append(char)
            if char in (")", "}", "]"):
                if stack != [] and mapping[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
            print(stack)
        
        return stack == []