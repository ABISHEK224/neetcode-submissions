class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*(len(temperatures))
        # [30,38,30,36,35,40,28]
        # [0,0,0,0,0,0,0]
        for i,t in enumerate(temperatures):
            while len(stack) and t > stack[-1][0]:
                stackelement , stackInd = stack.pop()
                res[stackInd] = i-stackInd
            stack.append((t,i))

        return res


            


