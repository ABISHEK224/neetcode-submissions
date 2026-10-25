class Solution:
    def climbStairs(self, n: int) -> int:
        cacheMap = {}

        def dfs(n):
            if n<=1:
                return 1
            
            if n in cacheMap:
                return cacheMap[n]
            
            cacheMap[n] = dfs(n-1) + dfs(n-2)
            return cacheMap[n]
        return dfs(n)

       
    
        
        