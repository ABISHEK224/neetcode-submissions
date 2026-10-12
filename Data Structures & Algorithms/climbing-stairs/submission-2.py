class Solution:
    def climbStairs(self, n: int) -> int:
        cacheMap = {}
        def dfs(n):
            if n in cacheMap:
                return cacheMap[n]
            if n <= 1:
                return 1 
            result = dfs(n-1) + dfs(n-2)
            cacheMap[n] = result
            return result
        return dfs(n)
    
        
        