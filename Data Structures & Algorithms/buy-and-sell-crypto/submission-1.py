class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l=0
        r=1
        while l<r and r< len(prices):
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit,prices[r]-prices[l])
            else:
                l=r
            r=r+1
        return maxProfit

        