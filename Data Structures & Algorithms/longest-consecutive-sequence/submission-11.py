class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = {}

        if len(nums)==0:
            return 0

        if len(nums) ==1:
            return 1
        for n in nums:
            hashMap[n] = 1
        endResult = 0
        currResult = 1

        for i in range(0,len(nums)):
            minimum = nums[i]
            if nums[i]-1 not in hashMap:
                currResult = 1

                while minimum+1 in hashMap:
                    currResult+=1
                    minimum=minimum+1

            endResult = max(currResult,endResult)
        return endResult
        
            


        