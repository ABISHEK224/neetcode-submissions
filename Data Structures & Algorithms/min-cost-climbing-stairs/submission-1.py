class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cacheMap = {}
        # startCost = min(cost[0],cost[1])
        
        def dfs(i):

            if i > len(cost)-1:
                return 0
            if i in cacheMap:
                return cacheMap[i]
            currentCost = cost[i]
    
            cacheMap[i]= currentCost + min(dfs(i+1),dfs(i+2))
            return cacheMap[i]

        return min(dfs(0),dfs(1))


            
                
            


            

        