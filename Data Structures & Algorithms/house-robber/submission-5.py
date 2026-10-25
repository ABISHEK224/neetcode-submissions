class Solution:
    def rob(self, nums: List[int]) -> int:
        cacheMap = {}

        def dfs(i):
            if i > len(nums)-1:
                return 0

            if i in cacheMap:
                return cacheMap[i]

            curr = nums[i]

            cacheMap[i] = max(curr + dfs(i+2), dfs(i+1))

            return cacheMap[i]


        return max(dfs(0), dfs(1))






        