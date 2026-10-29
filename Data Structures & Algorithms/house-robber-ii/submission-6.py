class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        if not len(nums):
            return 0
        if len(nums)==1:
            return nums[0]
        def dfs(i,flag):
            if i>len(nums)-1:
                return 0
            if i == len(nums)-1 and flag:
                return 0
            tup = (i,flag)

            if tup in memo:
                return memo[tup]
            curr = nums[i]
            memo[tup] = max(dfs(i+1,flag),curr +dfs(i+2,flag))
            return memo[tup]    
        return max(dfs(0,True),dfs(1,False))
        