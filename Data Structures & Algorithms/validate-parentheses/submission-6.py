class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)==1):
            return False
        stack = []
        paranthesesMap ={
                "(": ")",
                "[": "]",
                "{": "}"
            }
        for i in s:
            if i in paranthesesMap.keys():
                stack.append(i)
            elif i in paranthesesMap.values():
                if len(stack) and paranthesesMap[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0