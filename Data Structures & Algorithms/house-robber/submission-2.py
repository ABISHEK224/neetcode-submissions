class Solution:
    def rob(self, nums: List[int]) -> int:
        map={}
        i=0
        def dfs(i):
            if i>=len(nums):
                return 0
            if i in map:
                return map[i]
            result = max(nums[i]+dfs(i+2),dfs(i+1))
            map[i] = result
            return result
        return dfs(i)
    







        