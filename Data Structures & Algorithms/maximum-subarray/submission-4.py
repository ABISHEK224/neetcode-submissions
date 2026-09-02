class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=nums[0]
        maxSum = nums[0]

        for i in range(1,len(nums)):
            # print("current",current,nums[i],maxSum)
            if current < 0 or current + nums[i] < 0:
                current = nums[i]
            else:
                maxSum = max(current+nums[i],maxSum)
                current = current+nums[i]
        return max(maxSum,current)
        



        