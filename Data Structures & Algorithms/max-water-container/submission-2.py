class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0,len(heights)-1
        maxArea = 0
        while left<=right and right<len(heights):
            currentArea = (right-left)*min(heights[left],heights[right])
            if heights[left] < heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
            else:
                left+=1
            maxArea = max(maxArea,currentArea)
        return maxArea
        